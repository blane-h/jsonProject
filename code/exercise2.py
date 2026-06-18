# WRITE YOUR CODE HERE
def move_to_bottom(my_dict, my_key):
  if my_key not in my_dict:
    return "The key is not in the dictionary"
  else:
    value = my_dict[my_key]
    my_dict.pop(my_key)
    my_dict[my_key] = value
    return my_dict

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  move_to_bottom(example_dict, 4)
  print(example_dict)