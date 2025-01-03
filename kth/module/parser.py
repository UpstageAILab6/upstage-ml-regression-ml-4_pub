import pandas as pd

def 시_군_구_add(df):
    df[['시', '구', '동']] = df['시군구'].str.split(' ', expand=True)


def 아파트_unique_key_add(df):
    df['아파트_unique_key'] = df['구'] + "_" + df['동'] + "_" + df['번지'].astype(str) + "_" + df['아파트명'].astype(str) + "_" + df[
        '건축년도'].astype(str)

# 좌표X 기준으로 정렬 후, 첫 번째 값을 유지하여 채우는 함수
def fill_coordinates_sorted(df):
    df.sort_values(by='좌표X', inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.drop_duplicates(subset=['아파트_unique_key'], keep='first', inplace=True)

def 날짜포맷_add(df):
    df["계약연도"] = df["계약년월"].astype(str).str[:4]  # 첫 4글자는 연도
    df["계약월"] = df["계약년월"].astype(str).str[4:]  # 나머지 글자는 월

    # 계약월 컬럼을 1 -> 01, 2 -> 02 형태로 포맷을 변경합니다.
    df['계약일'] = df['계약일'].apply(lambda x: f'{x:02d}')

    # 계약 년월일(Y-m-d) 컬럼도 함께 생성해 줍시다.
    df["계약년월일"] = df["계약년월"].astype(str) + df["계약일"].astype(str)
    
def to_datetime(df, column_name):
    df[column_name] = pd.to_datetime(df[column_name])
