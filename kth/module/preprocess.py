from module import file_load
import pandas as pd
from scipy.spatial import KDTree

def 시_군_구_add(df):
    df[['시', '구', '동']] = df['시군구'].str.split(' ', expand=True)

def 번지주소_add(df):
    df['번지주소'] = df['시']  + ' ' + df['구'] + ' ' + df['동'] + ' ' + df['번지'].astype(str)

def 계약년도월일_add(df):
    df['계약년도-월-일'] = pd.to_datetime(df['계약년월'].astype(str) + df['계약일'].astype(str), format='%Y%m%d').astype(str)


def 금리_add(df):
    금리 = file_load.금리_file()
    금리['date'] = pd.to_datetime(금리['date'])  # date 컬럼을 datetime으로 변환
    금리 = 금리.set_index('date')

    계약년도월일_add(df)
    df['계약년도-월-일'] = pd.to_datetime(df['계약년도-월-일'])

    df['계약년도_6개월전'] = df['계약년도-월-일'] - pd.DateOffset(months=6)
    df['계약년도_1년전'] = df['계약년도-월-일'] - pd.DateOffset(years=1)
    df['계약년도_1년6개월전'] = df['계약년도-월-일'] - pd.DateOffset(years=1, months=6)
    df['계약년도_2년전'] = df['계약년도-월-일'] - pd.DateOffset(years=2)

    df['금리'] = df['계약년도-월-일'].apply(lambda x: 금리['rate'].get(x, None))
    df['금리_6개월전'] = df['계약년도_6개월전'].apply(lambda x: 금리['rate'].get(x, None))
    df['금리_1년전'] = df['계약년도_1년전'].apply(lambda x: 금리['rate'].get(x, None))
    df['금리_1년6개월전'] = df['계약년도_1년6개월전'].apply(lambda x: 금리['rate'].get(x, None))
    df['금리_2년전'] = df['계약년도_2년전'].apply(lambda x: 금리['rate'].get(x, None))

    return df

def 결측치_제거_100만개_이상(df):
    selected = list(df.columns[df.isnull().sum() <= 1000000])
    return df[selected]

def 범주형_타입변환(df):
    df['번지'] = df['번지'].astype('str')
    df['본번'] = df['본번'].astype('str')
    df['부번'] = df['부번'].astype('str')
    df['계약년월'] = df['계약년월'].astype('str')
    df['계약일'] = df['계약일'].astype('str')
    df['층'] = df['층'].astype('str')
    df['건축년도'] = df['건축년도'].astype('str')
    df['계약년월'] = df['계약년월'].astype('str')
    df['계약년월'] = df['계약년월'].astype('str')


def 날짜포맷_add(df):
    df["계약연도"] = df["계약년월"].astype(str).str[:4]  # 첫 4글자는 연도
    df["계약월"] = df["계약년월"].astype(str).str[4:]  # 나머지 글자는 월

    # 계약월 컬럼을 1 -> 01, 2 -> 02 형태로 포맷을 변경합니다.
    df['계약일'] = df['계약일'].apply(lambda x: f'{int(x):02d}' if x.isdigit() else x)

    # 계약 년월일(Y-m-d) 컬럼도 함께 생성해 줍시다.
    df["계약년월일"] = df["계약년월"].astype(str) + df["계약일"].astype(str)

def target이상체제거(df_target: pd.DataFrame):
    print('target이상체제거2111')
    # 계약년월일을 datetime 형식으로 변환
    df_target['계약년월일'] = pd.to_datetime(df_target['계약년월일'])

    # 그룹화 및 정렬
    sorted_df = df_target.sort_values(by=['시군구', '번지', '아파트명','평수', '계약년월일'])

    # 이전 가격 추가
    sorted_df['이전가격'] = sorted_df.groupby(['시군구', '번지', '아파트명','평수'])['target'].shift(1)

    # 하락률 계산
    sorted_df['하락률'] = ((sorted_df['target'] - sorted_df['이전가격']) / sorted_df['이전가격']) * 100

    # 35% 이상 하락한 경우 제거
    cond = (sorted_df['이전가격'].notnull()) & (sorted_df['하락률'] <= -35)

    return sorted_df[~cond]

def convert_m2_to_pyong(area_m2):
    return int(area_m2 / 3.3058)  # Truncate decimal places

def 평수_add(df):
    df["평수"] = df["전용면적(㎡)"].apply(convert_m2_to_pyong)


# KDTree를 사용하여 가장 가까운 지하철 거리 계산
def calculate_nearest_subway_distance(real_estate_df, taget_dt, target_name):
    # 지하철 위치로 KDTree 생성
    subway_tree = KDTree(taget_dt[['x', 'y']].values)

    # 부동산 위치에 대해 가장 가까운 지하철 거리 계산
    distances, _ = subway_tree.query(real_estate_df[['좌표X', '좌표Y']].values)

    # 거리 정보를 새로운 컬럼으로 추가
    real_estate_df[target_name] = distances
    real_estate_df[target_name] = real_estate_df[target_name].apply(lambda x: x * 100000)
    return real_estate_df

def calculate_nearest_bus_distance(real_estate_df, taget_dt, target_name):
    # 버스 위치로 KDTree 생성
    bus_tree = KDTree(taget_dt[['x', 'y']].values)

    # 부동산 위치에 대해 가장 가까운 버스 거리 계산
    distances, _ = bus_tree.query(real_estate_df[['좌표X', '좌표Y']].values)

    # 거리 정보를 새로운 컬럼으로 추가
    real_estate_df[target_name] = distances
    real_estate_df[target_name] = real_estate_df[target_name].apply(lambda x: x * 100000)
    return real_estate_df

# 1차 역세권: 역 승강장 경계로부터 250m 이내의 범위
# 2차 역세권: 역 승강장 경계로부터 250m에서 500m 이내의 범위
def 역세권_add(df):
    df['1차역세권'] = 0
    df['2차역세권'] = 0

    df.loc[df['nearest_subway_distance'] <= 250, '1차역세권'] = 1
    df.loc[(250 < df['nearest_subway_distance']) & (df['nearest_subway_distance'] <= 500), '2차역세권'] = 1

def 버세권_add(df):
    df['1차버스정류장'] = 0
    df.loc[df['nearest_bus_distance'] <= 250, '1차버스정류장'] = 1

def 건축년도_경과연도_categorize(df):
    def 건축년도_경과연도_categorize(years):
        if years >= 40:
            return '40년_경과'
        elif years >= 35:
            return '35년_경과'
        elif years >= 30:
            return '30년_경과'
        elif years >= 25:
            return '25년_경과'
        else:
            return '25년_이전'
    df['경과연도'] = df['계약연도'].astype(int) - df['건축년도'].astype(int)
    df['경과구분'] = df['경과연도'].apply(건축년도_경과연도_categorize)
    df.drop(['경과연도'], axis=1, inplace=True)