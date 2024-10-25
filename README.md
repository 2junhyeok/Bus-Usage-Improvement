본 프로젝트는 **'2024-1 딥러닝 수업'** 에서 진행한 프로젝트입니다. 

<br/>

## 👬 팀원
- 조현식, 이준혁, 권민지

## 🕓 기간
- 24.04.28 ~ 24.06.06

## 📑 주제
- 교통약자를 위한 버스 이용 개선 (feat. Object Detection & Pose estimation)
- 대상: 휠체어 이용자, 시각장애인

## 🖥 역할 
- 팀장, 발표, 아이디어 기획, 활용 데이터 탐색, 전반적인 Pipeline 구성, OpenPose Pipeline 구체화

<br/>

### 프로젝트 배경

<br/>

- https://www.youtube.com/watch?v=gGgLmX9bdKk&t=185s
- 해당 유튜브 영상에서는 휠체어 이용자가 버스를 탑승했으나 휠체어 우선 좌석이 비어있지 않았고 버스 기사 대응도 미흡
- 즉, 교통약자를 맞이할 준비가 전혀 되어 있지 않았고, 교통 약자는 불편한 공기를 느끼며 대중교통을 이용해야 한다는 게 대한민국 대중교통 이용 현실  
- 이러한 상황을 개선하기 위해 버스 승강장 카메라를 이용하여 시각 장애인과 휠체어 이용자를 탐지하고, 도착 예정 버스 운전기사와 승객에게 신호 전달하여 교통 약자를 맞이할 준비를 할 수 있도록 하는 시스템 구축


<br/>

### Pipeline 요약

<br/>

![4-1](https://github.com/user-attachments/assets/74b08331-e271-470e-b613-616bec767e7a)

<br/>

1. 버스정류장 CCTV에 라즈베리파이 설치
2. OpenCV를 사용하여 라즈페이 파이에서 실시간으로 버스정류장 CCTV 프레임 캡처
3. Frame Skipping, Resizing, Normalization, Color Space Conversion, Noise Reduction 진행
4. 야간에도 탐지 성능을 유지하기 위해 Zero-DCE 사용
5. 무선 통신 장치(LTE)를 통해 중앙 서버(SPARC)로 전처리된 데이터 전송
6. 중앙 서버에서 YOLOv10을 이용한 휠체어 이용자 탐지 및 OpenPose을 활용한 시각장애인 탐지
7. 객체 추적 알고리즘 DeepSort도 활용하여 동일 인물 탐지 및 버스 탑승 여부 확인
8. 추후 예측 모델 개발에 활용될 수 있도록 탐지 데이터를 데이터 베이스(Oracle,MySQL)에 저장
9. LTE와 연계 라우터를 사용하여 탐지된 객체 카운트 정보를 버스 기사 단말기에 전송하여 승객들에게 휠체어 이용자 또는 시각장애인 탑승 예정 정보를 청각 및 시각적으로 알림

<br/>

### 느낀점과 앞으로의 계획
- 본 프로젝트는 단순히 Pipline을 구성하는 거에 그쳤기 때문에 현실성이 부족한 부분이 존재할 가능성 O
- **'2024 국토교통 데이터활용 경진대회'** 참가하여 본 프로젝트를 디벨롭할 예정
- 추가로 '딥러닝' 수업을 수강한 학생들이 준 피드백도 적극 반영할 예정

<br/>

### 피드백
![4-2](https://github.com/user-attachments/assets/08f9ee62-c78c-433b-8181-d288c450e2db)
![4-3](https://github.com/user-attachments/assets/11fc9965-02b3-46d6-a13b-a8ad8ce5cc77)
![4-4](https://github.com/user-attachments/assets/605dbb19-89ac-4a15-af24-28b2329c7445)
![4-5](https://github.com/user-attachments/assets/3c10cdfd-8ba2-4fc5-944d-b4aa639fd177)
![4-6](https://github.com/user-attachments/assets/da3ecd1b-5018-41fe-b80c-49c84ba27632)
![4-7](https://github.com/user-attachments/assets/b57b8ce1-38d8-4e37-8128-1c7ee3b2cc6e)
![4-8](https://github.com/user-attachments/assets/1d816990-70b3-45f1-b153-7da91784c707)
![4-9](https://github.com/user-attachments/assets/3910d8a2-2d4e-4fa2-802d-9f45e2cc8500)







