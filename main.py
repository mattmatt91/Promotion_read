from datetime import datetime
import json as js
import os
from pathlib import Path
from colorama import Fore, Back, Style

# from readdata import read_data 

def read_json(filename):
    with open(filename) as json_file:
        return js.load(json_file)


def check_if_int(num):
    try:
        return int(num)
    except:
        return None

def get_path(properties):
    root_path_data = properties['path']
    last_dir = properties['lastdir']
    path = os.path.join(root_path_data, last_dir)
    return path

def start_measurement():
    # reading sample list
    properties = read_json('properties.json')
    samples = [i for i in properties['samples']]
    # reading properties

    # select path
    path = get_path(properties)
    exit()
    properties['lastdir'] = folder

    #select sample
    sample = select_sample(samples)
    properties["sample"]= sample

    #select height
    height = select_height()
    properties["height"]= height

    #select number of sample
    sample_number = set_number()
    properties['sample_number'] = sample_number

    #add info
    info = add_info()
    properties['info'] = info
    
    #setting timestamp
    properties["datetime"]= datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    # updating poperties global json
    update_properties(properties)
    
    # make dir for measurement
    path, path_file = mkdir(properties, folder)
    properties['path'] = path

    # saving properties for measurement
    save_properties_measurement(properties)

    # main measuring part
    read_data(properties, path_file)
###########################

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]  
    


def select_sample(samples):
    print('select sample')
    print('press:')
    for sample in samples:
        print(sample, 'for', samples[sample])
    sample = None
    while sample == None:
        user_input = input()
        try:
            sample = samples[user_input]
        except:
            print('samlple out of range')
    print(sample, ' selected')
    return sample

def select_height():
    print('select height')
    print('enter int in cm:')
    height = None
    while height == None:
        user_input = input()
        try:
            height = int(user_input)
        except:
            pass
    print('height: ', height, 'cm')
    return height

def set_number():
    print('select number')
    print('enter int:')
    sample_number = None
    while sample_number == None:
        user_input = input()
        try:
            sample_number = int(user_input)
        except:
            print('not an integer')
    print('number: ', sample_number)
    return sample_number

def add_info():
    user_input = input('add info')
    return user_input

def update_properties(properties):
    update_json = {}
    for item in "rate duration sensors path lastdir droptime".split():
        update_json[item]= properties[item]

    json_string = js.dumps(update_json)
    with open('properties.json', 'w') as outfile:
        outfile.write(js.dumps(json_string, indent=4))
    
def mkdir(properties, folder):
    name = properties['sample'] + '_' + str(properties['sample_number']) + '_' + str(properties['datetime'])
    path = os.path.join(properties['path'], folder, name)
    Path(path).mkdir(parents=True, exist_ok=True)
    path_file = os.path.join(path, name)
    path_file = path_file + '.txt'
    return path, path_file

def save_properties_measurement(properties):
    save_properties = properties
    del save_properties['lastdir']
    json_string = js.dumps(save_properties)
    json_name = properties['path'] + '\\info.json'
    with open(json_name, 'w') as outfile:
        outfile.write(js.dumps(json_string, indent=4))

    
if __name__ == '__main__':
    start_measurement()