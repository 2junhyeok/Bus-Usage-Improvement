import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from dataset import CustomImageDataset  # CustomImageDataset 클래스가 dataset.py에 있다고 가정
from ultralytics import YOLO

# Transform 정의
transform = transforms.Compose([
    transforms.Resize((640, 640)),
    transforms.ToTensor()
])

# 데이터셋 및 데이터로더 정의
train_dataset = CustomImageDataset(annotations_file='train_annotations.csv', img_dir='Images_RGB/Images_RGB', transform=transform)
train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)

# YOLOv10 모델 로드
model = YOLO('yolov10n.pt')  # YOLOv10 사전 학습된 모델

# GPU 사용 가능 시 GPU 설정
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# Optimizer 설정
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Loss 기록을 위해 정의
train_losses = []

# Custom Training Loop
num_epochs = 10
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for images, bboxes, labels in train_loader:
        images = images.to(device)
        
        # Prepare targets
        targets = []
        for i in range(len(bboxes)):
            xmin, ymin, xmax, ymax = bboxes[i]
            xmin, ymin, xmax, ymax = float(xmin), float(ymin), float(xmax), float(ymax)
            label = int(labels[i])  # 클래스 레이블을 정수로 변환
            
            targets.append({'boxes': torch.tensor([[xmin, ymin, xmax, ymax]]).to(device),
                            'labels': torch.tensor([label]).to(device)})
        
        # Forward pass
        optimizer.zero_grad()
        loss, _ = model(images, targets)  # model의 출력은 loss와 outputs 하나이므로, _로 outputs를 무시
        
        # Backward pass
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
    
    epoch_loss = running_loss / len(train_loader)
    train_losses.append(epoch_loss)
    print(f"Epoch {epoch+1}/{num_epochs}, Training Loss: {epoch_loss}")

# 학습된 모델 저장
model.save('custom_yolov10.pt')
