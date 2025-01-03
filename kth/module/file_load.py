import pandas as pd

# 파생변수 추가할떄마다 버전이 증거함
current_version = 'v7'

# 초기 버전 수정하지 않음
origin_train_path = '../data/train_origin.csv'
origin_test_path = '../data/test_origin.csv'

unique_apt_group_file_name = '../data/unique_apt_group.csv'
apt_xy_file_path = '../data/unique_apt_group_xy.csv'
금리_file_name = '../data/interest_rate.csv'

sub_feature_path = '../data/subway_feature.csv'
bus_feature_path = '../data/bus_feature.csv'

def loadVersionOfData(version):
    return pd.read_csv(f'../data/{version}.csv', low_memory=False)

def load_origin_train():
    return pd.read_csv(origin_train_path, low_memory=False)

def load_origin_test():
    return pd.read_csv(origin_test_path, low_memory=False)

def load_origin_data():
    train = load_origin_train()
    test = load_origin_test()

    train['is_test'] = 0
    test['is_test'] = 1
    return pd.concat([train, test], axis=0)

def load_current_version():
    train = loadVersionOfData(f'train_{current_version}')
    test = loadVersionOfData(f'test_{current_version}')
    train['is_test'] = 0
    test['is_test'] = 1
    return pd.concat([train, test], axis=0)

def unique_apt_group_file():
    return pd.read_csv(unique_apt_group_file_name, low_memory=False)

def load_apt_xy_file_path():
    return pd.read_csv(apt_xy_file_path, low_memory=False)

def 금리_file():
    return pd.read_csv(금리_file_name, low_memory=False)

def load_지하철():
    return pd.read_csv(sub_feature_path, low_memory=False)

def load_버스():
    return pd.read_csv(bus_feature_path, low_memory=False)
