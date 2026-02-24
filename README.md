# 🐱 Dog vs 🐶 Cat Classifier (Xception)

이 프로젝트는 **TensorFlow**의 **Xception** 모델을 사용하여 강아지와 고양이를 분류하는 웹 서비스입니다. **Gradio**를 활용하여 누구나 쉽게 이미지를 업로드하고 결과를 확인할 수 있습니다.

---

## 🚀 주요 기능
* **실시간 이미지 분류**: 이미지를 드래그 앤 드롭하면 즉시 강아지/고양이 확률을 계산합니다.
* **고성능 전처리**: 이미지 크기 조정(299x299), 흑백/RGBA 이미지 보정 로직이 포함되어 있습니다.
* **직관적인 인터페이스**: 예측 결과를 막대 그래프(Label) 형식으로 시각화하여 보여줍니다.

---

## 🛠️ 설치 및 실행 방법

### 1. 가상환경 활성화 (선택)
```bash
# 가상환경이 있다면 활성화 후 진행하세요.
# 예: conda activate DL

```

### 2. 필수 라이브러리 설치

이 프로젝트는 **Gradio v3/v4** 환경에 최적화되어 있습니다. 아래 명령어로 필요한 패키지를 설치하세요.

```bash
pip install "gradio<5.0" tensorflow numpy pillow

```

### 3. 모델 파일 확인

프로젝트 폴더 내에 학습된 모델 파일이 있는지 확인하세요.

* 파일명: `best_model_xception.keras`

### 4. 서비스 실행

```bash
python app.py

```

터미널에 표시되는 로컬 주소(`http://127.0.0.1:7860`)로 접속하면 서비스를 이용할 수 있습니다.

---

## 📂 파일 구조

* `app.py`: Gradio UI 구성 및 이미지 예측 핵심 로직
* `best_model_xception.keras`: 훈련된 Xception 모델 가중치 파일
* `README.md`: 프로젝트 설명 및 설치 가이드

---

## 📝 개발 노트

* **Input Size**: 299 x 299 (Xception 기본 규격)
* **Pre-processing**: `tf.keras.applications.xception.preprocess_input` 사용
* **Model Layer**: 출력 노드가 2개(Softmax) 또는 1개(Sigmoid)인 경우 모두 대응 가능하도록 설계됨

```
