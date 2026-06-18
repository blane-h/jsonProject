# WRITE YOUR CODE HERE
import json
def compare(path_1, path_2):
  with open(path_1) as file1, open(path_2) as file2:
    dict_1 = json.load(file1)
    dict_2 = json.load(file2)
  if dict_1 == dict_2:
    return "The dictionaries are equal"
  elif len(dict_1) == len(dict_2):
    return "Dictionary 1 and dictionary 2 have the same length"
  elif len(dict_1) > len(dict_2):
    return "Dictionary 1 is longer than dictionary 2"
  else:
    return "Dictionary 2 is longer than dictionary 1"

  
# test code below
