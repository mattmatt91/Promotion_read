from datetime import datetime
import json as js
import os
from pathlib import Path
from colorama import Fore, Back, Style
import pandas as pd
import plotly.express as px
import numpy as np
# from readdata import read_data


def start_measurement():
    properties = read_json('properties.json')
    path = os.path.join(properties['path'], properties['lastdir'])
    properties_measurement = properties.copy()
    properties_measurement["datetime"] = datetime.now().strftime(
        "%d-%m-%Y_%H-%M-%S")
    properties_measurement["number"] = properties["sample_counts"][properties["sample"]]
    properties["sample_counts"][properties["sample"]] += 1
    path = mk_dir_measurement(properties_measurement, path)
    for i in ['sample_counts', 'lastdir', 'path']:
        properties_measurement.pop(i)
    save_json(properties, 'properties.json')
    save_json(properties_measurement, os.path.join(path, 'properties.json'))
    # df = read_data(properties)
    df = create_test_df(properties)
    save_df(df, path)
    fig = px.line(
        df, title=properties_measurement["sample"] + '_' + str(properties_measurement['number']))
    fig.write_html(os.path.join(path, "quickplot.html"))
    # fig.show()


def create_test_df(properties):
    data = {}
    data['time'] = np.arange(
        0, properties['duration']-properties['droptime'], 1/properties['rate'])
    for sensor in properties['sensors']:
        data[sensor] = [np.random.randint(10) for _ in range(
            int(properties['rate']*(properties['duration']-properties['droptime'])))]
    df = pd.DataFrame(data)

    df.set_index('time', inplace=True)
    return df


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
    df.to_csv(os.path.join(path, 'data.csv'),
              decimal=',', sep=';', index=True)


if __name__ == '__main__':
    start_measurement()
