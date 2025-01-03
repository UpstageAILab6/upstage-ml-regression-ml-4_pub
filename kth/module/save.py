# v1 : xy좌표 추가

def save_version(df, vesion):
    dt_train = df.query('is_test == 0')
    dt_test = df.query('is_test == 1')

    dt_train.drop(['is_test'], axis=1, inplace=True)
    dt_test.drop(['is_test'], axis=1, inplace=True)

    dt_train.to_csv(f'../data/train_{vesion}.csv', index=False)
    dt_test.to_csv(f'../data/test_{vesion}.csv', index=False)
    print(f'{vesion}.csv 파일이 저장되었습니다.')