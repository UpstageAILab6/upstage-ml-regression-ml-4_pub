[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/pjJxrz8e)
# ML 경진대회 | House Price Prediction 
## Team Ravenclaw
| ![정혜린](https://avatars.githubusercontent.com/u/156163982?v=4) | ![강태화](https://avatars.githubusercontent.com/u/156163982?v=4) | ![정준성](https://avatars.githubusercontent.com/u/156163982?v=4) | ![정인복](https://avatars.githubusercontent.com/u/156163982?v=4)  | 
| :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: | 
|            [정혜린](https://github.com/UpstageAILab)             |            [강태화](https://github.com/wooobo/upstage-ml-regression-ml)             |            [정준성](https://github.com/UpstageAILab)             |            [정인복](https://github.com/UpstageAILab)              |            
|                            팀장 / 분석 및 모델링                  |                           팀원 / 분석 및 모델링                   |                            팀원 / 분석 및 모델링                 |                            팀원 / 분석 및 모델링                 |                                                       

## 0. Overview
### Environment
- AI stages의 서버에 연결한 vscode

### Requirements
- numpy == 1.23.5
- pandas == 1.5.3
- scikit-learn == 1.2.2

## 1. Competiton Info
### Overview

<소개 및 배경 설명>
- 1. ML 알고리즘을 활용하여 미래의 매매가 예측을 통해 더욱 효율적인 부동산
거래환경 조성 및 의사결정 제공
- 2. 부동산 시장과 실거래가의 중요성 : 실거래가는 실제 시장에서 거래된
가격을 뜻하므로, 실질적인 한국의 가계 정도 유추 가능
- 3. ML 도입의 필요성 : 다차원적 요인 분석과 높은 예측 정확도를 통해 부동산
시장을 보다 체계적으로 이해할 수 있는 가능성 제공

<목표>
* 내/외부 데이터를 활용한 데이터 수집, 처리 및 분석
* 다양한 ML regression 모델 이해하고 적용
* 하이퍼파라미터 튜닝을 통한 모델 예측 score 향상

### Timeline
- January 02, 2025 - Start Date
- January 07, 2025 - Final submission deadline

## 2. Components
### Directory
```
├── README.md
├── code
|   ├── trainvalid_HR.ipynb
|   └── trainvalid_HR.py
├── output
|   └── output_HR.csv
└── result
    └── prediction_result.pdf 
```


## 3. Data descrption
### Dataset overview
-![image](https://github.com/user-attachments/assets/3bccd308-df12-46be-95cf-08e20cf93291)

### EDA
- ![image](https://github.com/user-attachments/assets/a45718ef-fb88-4122-b47b-594656fa2587)
- ![image](https://github.com/user-attachments/assets/8fcfeaba-8a68-43cc-9c1d-18b531eb6d85)

### Data Processing
- target의 log transformation시도
- 전용면적 변수에 대한 전처리 수행
- ![image](https://github.com/user-attachments/assets/cfdff4ac-150d-46f5-8f3d-632337f247c5)

## 4. Modeling
### Model descrition
#### Model(1)_정준성님
1. Randomforest regressor 
  - dataset : Train_(918680,63) /  Validation_(183736,63)
  - 중요한 feature TOP 3 : 전용면적, 권역, 매매지수
  - RMSE : 8860
    
#### Model(2)_정혜린님
2-1. lightGBM regressor (Hold out split, 리더보드에 올린 모델)
  - dataset : Train_(86684,26) /  Validation_(21672,63)
  - 중요한 feature TOP 3 : 계약년월, 전용면적, 층
  - RMSE : 13211.28
    
2-2. lightGBM regressor (TimeSeries split, n_splits = 5, 추가 시도했던 모델)
  - dataset : Train_(86684,26) /  Validation_(21672,63)
  - 중요한 feature TOP 5 : 좌표X, 좌표Y, 건축년도, 계약년월, 지하철역과의 거리
  - RMSE : 18937.04

#### Model(3)_강태화님
3. Randomforest regressor 
  - dataset : Train_(,50) /  Validation_(,50)
  - 중요한 feature TOP 3 : 계약년월, 가까운공원ID, 평수
  - RMSE : 17874.81

### Modeling Process
- ![image](https://github.com/user-attachments/assets/ce39ba02-37ef-4df8-9c2c-3ee4bfd17104)
- ![image](https://github.com/user-attachments/assets/0cb76923-6e6f-4933-a208-9f0d9375aa7e)
- ![image](https://github.com/user-attachments/assets/88c80b96-1796-4ba8-a5f9-a3bade25f658)

## 5. Result
### Leader Board
- ![image](https://github.com/user-attachments/assets/db704aad-6dc1-48e6-84cc-43c4db9bc48f)
** 최종 Selected model :
      - Randomforest regressor
      - dataset : Train_(918680,63) /  Validation_(183736,63)
      - 중요한 feature TOP 3 : 전용면적, 권역, 매매지수
      - LOCAL RMSE : 8860
      - PUBLIC RMSE : 16406.0449

### Presentation
- https://github.com/UpstageAILab6/upstage-ml-regression-ml-4/blob/main/result/prediction_result.pdf

## etc
### Meeting Log
- Slack, Zoom, GoogleMeet

### Reference
- https://developers.kakao.com/docs/latest/ko/local/dev-guide#search-by-keyword
- https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1073
- https://www.bigdata-forest.kr/product/PTP019701
- https://www.k-apt.go.kr/web/board/webReference/boardList.do
