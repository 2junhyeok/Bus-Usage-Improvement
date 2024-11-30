import torch
from ultralytics import YOLO
import cv2
from matplotlib import pyplot as plt

# YOLO 모델 로드 (학습된 모델 경로 지정)
model = YOLO('custom_yolov10.pt')  # 학습된 모델 파일 경로

# 테스트할 이미지 경로 설정
image_path = 'wheelchair.png'

# 이미지 로드
img = cv2.imread(image_path)
if img is None:
    raise FileNotFoundError(f"{image_path} does not exist")

# 이미지에서 객체 탐지
results = model(image_path)

# 결과 시각화 및 저장
def plot_boxes(image, results):
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].int().cpu().numpy()  # CPU로 복사
            conf = box.conf.item()
            cls = box.cls.item()
            label = f'{model.names[int(cls)]} {conf:.2f}'
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    return image

# 탐지된 결과를 이미지에 그리기
img_with_boxes = plot_boxes(img.copy(), results)

# 결과 이미지 저장 및 표시
result_image_path = 'wheelchair_detection.png'
cv2.imwrite(result_image_path, img_with_boxes)

# 이미지 출력
plt.imshow(cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
