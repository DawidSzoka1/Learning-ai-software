import pandas as pd

def prep_data(file_name):
    data = pd.read_csv(file_name, header=[0, 1], index_col=0)
    return data

def get_atr_for_city(atr_name, city_name, data):
    return data[city_name][atr_name].to_numpy()

