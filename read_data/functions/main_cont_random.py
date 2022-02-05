"""
This is a test mudule of this repository.
It creates random data sets with random parameters
for testing the process_data moule
"""

from datetime import datetime
import json as js
import os
from pathlib import Path
import main as mn

from readdata_dummy import read_data 


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
        read_data(properties, path_file)
    
if __name__ == '__main__':
    start_measurement(3)