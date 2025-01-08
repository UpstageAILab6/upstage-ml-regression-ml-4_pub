[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/pjJxrz8e)
# Title (Please modify the title)
## Team

| ![박패캠](https://avatars.githubusercontent.com/u/156163982?v=4) | ![이패캠](https://avatars.githubusercontent.com/u/156163982?v=4) | ![최패캠](https://avatars.githubusercontent.com/u/156163982?v=4) | ![김패캠](https://avatars.githubusercontent.com/u/156163982?v=4) | ![오패캠](https://avatars.githubusercontent.com/u/156163982?v=4) |
| :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: |
|            [박패캠](https://github.com/UpstageAILab)             |            [이패캠](https://github.com/UpstageAILab)             |            [최패캠](https://github.com/UpstageAILab)             |            [김패캠](https://github.com/UpstageAILab)             |            [오패캠](https://github.com/UpstageAILab)             |
|                            팀장, 담당 역할                             |                            담당 역할                             |                            담당 역할                             |                            담당 역할                             |                            담당 역할                             |

## 0. Overview
### Environment
- AI stages의 서버에 연결한 vscode

### Requirements
- _Write Requirements_

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

- ex) January 02, 2025 - Start Date
- ex) January 07, 2025 - Final submission deadline

## 2. Components

### Directory

- '/data/ephemeral/home/'


## 3. Data descrption

### Dataset overview

- _Explain using data_

### EDA

- _Describe your EDA process and step-by-step conclusion_

### Data Processing

- _Describe data processing process (e.g. Data Labeling, Data Cleaning..)_

## 4. Modeling

### Model descrition

- 1. Randomforest regressor
         dataset : Train_(918680,63) /  Validation_(183736,63)
         중요한 feature TOP 3 : 전용면적, 권역, 매매지수
         RMSE : 8860
- 2. lightGBM regressor
         dataset : Train_(86684,26) /  Validation_(21672,63)
         중요한 feature TOP 3 : 계약년월, 전용면적, 층
         RMSE : 13211.28
-3. Randomforest regressor
         dataset : Train_(,50) /  Validation_(,50)
         중요한 feature TOP 3 : 계약년월, 가까운공원ID, 평수
         RMSE : 17874.81
         
### Modeling Process

- ![image](https://github.com/user-attachments/assets/ce39ba02-37ef-4df8-9c2c-3ee4bfd17104)
- ![image](https://github.com/user-attachments/assets/0cb76923-6e6f-4933-a208-9f0d9375aa7e)
- ![image](https://github.com/user-attachments/assets/88c80b96-1796-4ba8-a5f9-a3bade25f658)

## 5. Result

### Leader Board

- ![image](https://github.com/user-attachments/assets/db704aad-6dc1-48e6-84cc-43c4db9bc48f)


- Randomforest regressor
         dataset : Train_(918680,63) /  Validation_(183736,63)
         중요한 feature TOP 3 : 전용면적, 권역, 매매지수
         LOCAL RMSE : 8860
         PUBLIC RMSE : 16406.0449

### Presentation

- _Insert your presentaion file(pdf) link_

## etc

### Meeting Log

- _Insert your meeting log link like Notion or Google Docs_

### Reference

- _Insert related reference_
