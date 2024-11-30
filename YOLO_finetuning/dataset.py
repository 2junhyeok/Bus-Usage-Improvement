import os
import pandas as pd
from PIL import Image
from torch.utils.data import Dataset

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None):
        self.annotations = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        
        # 클래스를 정수로 매핑하는 딕셔너리 생성
        self.class_to_int = {
            'person': 0,
            'wheelchair': 1,
        }

        # 유효한 클래스만 포함하는 데이터만 남깁니다.
        self.annotations = self.annotations[self.annotations['class'].isin(self.class_to_int.keys())]

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.annotations.iloc[idx, 0])
        image = Image.open(img_path).convert("RGB")
        
        label_str = self.annotations.iloc[idx, 3]
        label = self.class_to_int[label_str]

        xmin = float(self.annotations.iloc[idx, 4])
        ymin = float(self.annotations.iloc[idx, 5])
        xmax = float(self.annotations.iloc[idx, 6])
        ymax = float(self.annotations.iloc[idx, 7])

        bboxes = [[xmin, ymin, xmax, ymax]]  # bounding box 좌표를 리스트로 반환

        if self.transform:
            image = self.transform(image)

        return image, bboxes, label
