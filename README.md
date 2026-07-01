# Diabetes-prediction

🌐 **Live Demo**: https://diabetes-prediction-bridy.streamlit.app/

# 🩺 당뇨병 위험도 예측 시스템

## 프로젝트 개요

Behavioral Risk Factor Surveillance System (BRFSS) 2015 데이터셋을 활용하여
개인의 건강 정보와 생활습관을 입력하면 당뇨병 위험도를 예측하는 머신러닝 모델과 웹 애플리케이션을 개발했습니다.

생명과학 석사 및 연구원 경력을 바탕으로 데이터 분석 결과에 의학적 해석을 더했습니다.

---

## 데이터셋

- **출처**: Kaggle - Diabetes Health Indicators Dataset (BRFSS 2015)
- **데이터 크기**: 253,680명, 22개 변수
- **목표 변수**: 당뇨병 여부 (Diabetes / Non-Diabetes)

---

## 주요 분석 내용

### 1. 데이터 전처리

- 결측치 여부 확인
- 다중 클래스(0, 1, 2) 데이터를 이진 분류(0, 1)로 변환
- Train/Test Split (Stratified Sampling)
- 클래스 불균형 확인 및 class_weight 적용

### 2. 탐색적 데이터 분석 (EDA)

- BMI와 당뇨병의 관계 분석
- 고혈압 여부와 당뇨병 발생률 비교
- 연령 증가에 따른 당뇨병 비율 분석
- 변수 중요도(Feature Importance) 분석

### 3. 주요 발견

- **BMI**가 증가할수록 당뇨병 위험이 증가하는 경향을 확인
- **고혈압** 환자에서 당뇨병 비율이 더 높게 나타남
- **연령**이 증가할수록 당뇨병 발생률이 증가하는 경향을 확인
- **주관적 건강 상태(General Health)** 역시 중요한 예측 변수로 확인됨

### 4. 머신러닝 모델

| 항목 | 결과 |
|------|------|
| 모델 비교 | Random Forest / XGBoost |
| 최종 모델 | XGBoost Classifier |
| Accuracy | 약 84% |
| Threshold | 0.3 적용 |
| 목적 | 당뇨 환자의 재현율 향상 |

기본 Threshold(0.5)에서는 당뇨 환자를 놓치는 비율이 높아,
Threshold를 0.3으로 조정하여 실제 의료 스크리닝 목적에 적합하도록 개선했습니다.

### 5. 변수 중요도 Top 5

1. BMI
2. Age
3. Income
4. Physical Health
5. General Health

---

## 웹 애플리케이션

Streamlit을 활용하여 사용자의 건강 정보를 입력하면
당뇨병 발생 위험도(%)와 위험 수준을 실시간으로 예측하는 웹 애플리케이션을 개발했습니다.

입력 항목은 다음과 같습니다.

- BMI
- 고혈압 여부
- 고콜레스테롤 여부
- 흡연 여부
- 운동 여부
- 연령
- 학력
- 소득 수준
- 건강 상태 등

---

## 실행 방법

```bash
pip install streamlit
streamlit run app.py
```

---

## 기술 스택

- **Language**: Python
- **Library**: pandas, numpy, scikit-learn, xgboost, matplotlib, streamlit, joblib
- **Model**: XGBoost Classifier

---

## 파일 구조

```
Diabetes-prediction/
├── Diabetes_prediction.ipynb        # 데이터 전처리 및 머신러닝
├── app.py                           # Streamlit 웹 애플리케이션
├── model.pkl                        # 학습된 모델
└── diabetes_012_health_indicators_BRFSS2015.csv
```

---

## Future Work

- SHAP을 이용한 예측 근거 시각화
- 하이퍼파라미터 최적화
- ROC-AUC 기반 모델 성능 개선
- 의료진 친화적인 UI 및 사용자 경험 개선
