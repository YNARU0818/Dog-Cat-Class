import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# Xception 모델 로드
model_path = 'best_model_xception.keras'
try:
    model = tf.keras.models.load_model(model_path)
    print("모델 로드 성공!")
    # 모델의 input_shape 확인 (일반적인 Xception 사이즈인 299x299로 기본 세팅)
    if model.input_shape[1] is not None and model.input_shape[2] is not None:
        input_shape = model.input_shape[1:3]
    else:
        input_shape = (299, 299)
except Exception as e:
    print(f"모델 로드 실패: {e}")
    model = None
    input_shape = (299, 299)

def predict(image):
    if model is None:
        return {"에러": "모델이 정상적으로 로드되지 않았습니다."}
    
    if image is None:
        return {"에러": "이미지를 입력해주세요."}

    # 1. 이미지 크기 조정 (모델의 기대 입력 크기에 맞게)
    img = Image.fromarray(image).resize(input_shape)
    img_array = np.array(img).astype('float32')
    
    # RGB 채널이 아닌 경우 (예: 흑백 이미지) 보정
    if len(img_array.shape) == 2:
        img_array = np.stack((img_array,)*3, axis=-1)
    elif img_array.shape[2] == 4: # RGBA
        img_array = img_array[:,:,:3]
        
    # 2. 배치 차원 추가 (batch_size, height, width, channels)
    img_array = np.expand_dims(img_array, axis=0)
    
    # 3. 데이터 전처리 (Xception 기본 전처리 사용, 보통 -1 ~ 1로 스케일링)
    # *참고: 학습할 때 1/255 스케일링을 사용했다면 이 부분을 img_array / 255.0 으로 수정해야 할 수 있습니다.
    processed_img = tf.keras.applications.xception.preprocess_input(img_array)
    
    # 4. 예측 수행
    prediction = model.predict(processed_img)[0]
    
    # 5. 결과 해석
    # 출력 노드가 1개인 경우 (Sigmoid)
    if len(prediction) == 1:
        prob_dog = float(prediction[0])
        prob_cat = 1.0 - prob_dog
    # 출력 노드가 2개 이상인 경우 (Softmax) - 알파벳 순서(Cat, Dog)로 가정
    else:
        prob_cat = float(prediction[0])
        prob_dog = float(prediction[1])
        
    # 퍼센트로 표시하기 위해 딕셔너리로 반환 (Gradio Label 컴포넌트용)
    return {
        "강아지 (Dog)": prob_dog,
        "고양이 (Cat)": prob_cat
    }

# Gradio 웹 인터페이스 정의
# 수정 후 코드
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(label="분류할 이미지를 업로드하세요"),
    outputs=gr.Label(num_top_classes=2, label="예측 결과"),
    title="🐱 고양이 vs 🐶 강아지 분류 서비스",
    description="제공해주신 `best_model_xception.keras` 모델을 사용하여 이미지가 고양이인지 강아지인지 판별합니다. 사진을 업로드하고 결과를 확인해보세요!",
    allow_flagging="never"
)
if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False)

