import numpy as np

from Ai.Numpy.practices.analizeCsvFiles.tools import prep_data

data = prep_data("dane_pogodowe.csv")
print(data['Warszawa'].keys())
def get_simple_stats(data, city_name):
    stats = {}
    for key in data[city_name].keys():
        np_array = data[city_name][key].to_numpy()
        stats[key] = {
            'min': np_array.min(),
            'max': np_array.max(),
            'mean': np_array.mean(),
            'median': np.median(np_array)
        }
    return stats

print(get_simple_stats(data, "Warszawa"))