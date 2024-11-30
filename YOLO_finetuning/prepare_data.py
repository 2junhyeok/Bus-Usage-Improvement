import os
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split

# 경로 설정
annotations_dir = 'Annotation/Annotation_RGB'
images_dir = 'Images_RGB/Images_RGB'

# 데이터 프레임 초기화
data = {
    'filename': [],
    'width': [],
    'height': [],
    'class': [],
    'xmin': [],
    'ymin': [],
    'xmax': [],
    'ymax': []
}

# Annotation 파일 읽기
for filename in os.listdir(annotations_dir):
    if filename.endswith('.yml') or filename.endswith('.yaml'):
        filepath = os.path.join(annotations_dir, filename)
        with open(filepath, 'r') as file:
            annotation = yaml.safe_load(file)
        
        img_filename = annotation['annotation']['filename']
        width = annotation['annotation']['size']['width']
        height = annotation['annotation']['size']['height']
        
        # 'object' 키가 존재하는지 확인
        objects = annotation['annotation'].get('object', [])
        if not isinstance(objects, list):
            objects = [objects]
        
        for obj in objects:
            cls = obj['name']
            bbox = obj['bndbox']
            xmin = int(bbox['xmin'])
            ymin = int(bbox['ymin'])
            xmax = int(bbox['xmax'])
            ymax = int(bbox['ymax'])
            
            data['filename'].append(img_filename)
            data['width'].append(width)
            data['height'].append(height)
            data['class'].append(cls)
            data['xmin'].append(xmin)
            data['ymin'].append(ymin)
            data['xmax'].append(xmax)
            data['ymax'].append(ymax)

# 데이터 프레임 생성
df = pd.DataFrame(data)

# Annotation 및 이미지 파일이 매칭되지 않는 경우 제거
df = df[df['filename'].apply(lambda x: os.path.exists(os.path.join(images_dir, x)))]

# 데이터 분할
train_df, temp_df = train_test_split(df, test_size=0.3, random_state=42)
val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)

# CSV 파일로 저장
train_df.to_csv('train_annotations.csv', index=False)
val_df.to_csv('val_annotations.csv', index=False)
test_df.to_csv('test_annotations.csv', index=False)

print(f"Training annotations: {len(train_df)}")
print(f"Validation annotations: {len(val_df)}")
print(f"Testing annotations: {len(test_df)}")
