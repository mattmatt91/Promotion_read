"""
This is a test mudule of this repository.
It creates random data sets with random parameters
for testing the process_data moule
"""

from __future__ import absolute_import, division, print_function

from datetime import datetime
import main as mn
import pandas as pd
import numpy as np
from random import randrange
import random


def generate_data(properties, path):
    """
    This funcion generates a dumme dataset and saves it to the path

    Args:
        properties (dictionary): dictionary with all parameters for the measurement
        path (string): path to the measurement file
    """
    rate = properties['rate']
    max_samples = rate*properties['duration']
    data = []
    for i in range(max_samples):
        this_samples = (i%200000)
        this_data = [np.sin(this_samples), np.sin(this_samples//2), np.sin(this_samples*2), np.tan(this_samples), np.tan(this_samples//2), np.tan(this_samples*2)]
        this_data = [i*random.uniform(0, 1) for i in this_data]
        data.append(this_data)
    df = pd.DataFrame(data, columns=properties['sensors'])
    df['time [s]'] = [i/rate for i in df.index]
    df.set_index('time [s]', inplace=True) 
    print(df.head())
    print(df.info())
    df.to_csv(path, sep='\t', decimal='.', index=True)
    # df.plot()
    # plt.show()

def start_measurement(number_of_measurement):
    """
    This is the main funciton of the module.
    It runs multiple random data sets.

    Args:
        number_of_measurement (int): number of datasets to create
    """
    # reading sample list
    samples = mn.read_json('samples.json')

    # reading properties
    properties = mn.read_json('properties.json')
    # select path
    folder, path = mn.get_path(properties)

    for i in range(number_of_measurement):
        # reading properties
        properties = mn.read_json('properties.json')
        # select path
        properties['lastdir'] = folder
        #select sample
        sample = samples[str((i%5+1))]
        print('sample is {0}'.format(sample))
        properties["sample"]= sample

        #select height
        height = 50
        print('height is {0}'.format(height))
        properties["height"]= height

        #select number of sample
        sample_number = i
        print('number is {0}'.format(sample_number))
        properties['sample_number'] = sample_number

        #add info
        info = "this is measurement number {0}".format(i)
        properties['info'] = info
        
        #setting timestamp
        properties["datetime"]= datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

        # updating poperties global json
        mn.update_properties(properties)
        
        # make dir for measurement
        path, path_file = mn.mkdir(properties, folder)
        properties['path'] = path

        # saving properties for measurement
        mn.save_properties_measurement(properties)

        # main measuring part
        generate_data(properties, path_file)
    
if __name__ == '__main__':
    start_measurement(3)