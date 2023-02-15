from datetime import datetime
import json as js
import os
from pathlib import Path
from colorama import Fore, Back, Style
import pandas as pd

# from readdata import read_data 





def start_measurement():
    properties = read_json('properties.json')
    path = os.path.join(properties['path'], properties['lastdir'])
    properties_measurement = properties.copy()
    properties_measurement["datetime"]= datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    properties_measurement["number"]= properties["sample_counts"][properties["sample"]]
    properties["sample_counts"][properties["sample"]] += 1
    path = mk_dir_measurement( properties_measurement,path)
    for i in ['sample_counts', 'lastdir', 'path']:
        properties_measurement.pop(i)
    save_json(properties, 'properties.json')
    save_json(properties_measurement, os.path.join(path,'properties.json'))
    df = pd.DataFrame({'A':[1,2,3], 'B':[4,6,8]})
    save_df(df, path)
       
def read_json(filename):
    with open(filename) as json_file:
        return js.load(json_file)
    
def mk_dir_measurement(properties, path):
    name = properties['sample'] + '_' + str(properties['number'])
    path = os.path.join(properties['path'], properties['lastdir'], name)
    Path(path).mkdir(parents=True, exist_ok=True)
    return path

def save_json(prop_dict, path):
    json_string = js.dumps(prop_dict, indent=3)
    print(path)
    with open(path, 'w') as outfile:
        outfile.write(json_string)

def save_df(df, path):
    df.to_csv(os.path.join(path, 'data.csv'),decimal=',',sep=';', index=False)
if __name__ == '__main__':
    start_measurement()