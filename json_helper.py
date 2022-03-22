from glob import glob
import json
import os
import pickle



"""
Part A
Create a program called json_helper.py
Define a function called read_json. Given a string 
representing a file path to a json file, this function 
should open said file and convert its contents into a 
json object.The json object should be returned.

"""
def read_json(path_name):
    file_name = path_name
    with open(file_name) as f_name:
        data = json.load(f_name)
    print(data)


path_name = ""
read_json("/Users/madhavirockandla/Python9Ex/data/super_smash_bros/link.json")


"""
Part B
Define a function called read_all_json_files. Given a string 
representing a path to a directory, this function should 
read all of the json files and return a list containing 
all of the json objects.Make sure to incorporate the work from part A.
"""
def read_all_json_files(path_name):
    my_pc = os.path.join(path_name, '*.json')
    for file_name in glob(my_pc):
        with open(file_name) as f_name:
            data = json.load(f_name)
        print(data)


path_name = ""
read_all_json_files(path_name)


"""
Part C
Define a function called write_pickle. This function should take 
a file path and some data. Given these parameters, the function 
should write the contents of the json files to a file called 
super_smash_characters.pickle.
"""


def write_pickle(dump_to_path, pickle_path):
    pickle_out = open(dump_to_path, "wb")
    pickle.dump(pickle_path, pickle_out)
    pickle_out.close()

    return


write_pickle("/Users/madhavirockandla/Python9Ex/data/super_smash_bros/super_smash_characters.pickle",
             "/Users/madhavirockandla/Python9Ex/data/super_smash_bros/mario.json")

"""
Part D
Define a function called load_pickle. Given a file path, this 
function opens a pickled file and returns the data.
Use this function to print the pickled data from Part C to the screen.

"""
def load_pickle():
    pickle_in = open("/Users/madhavirockandla/Python9Ex/data/super_smash_bros/"
                     "super_smash_characters.pickle", "rb")
    read_file = pickle.load(pickle_in)
    print(read_file)


load_pickle()

