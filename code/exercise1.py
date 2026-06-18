# WRITE YOUR CODE HERE
def find_key(my_dict, val):
  for k,v in my_dict.items():
    if v == val:
      return k
  return "not found"

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : ['red', 'blue', 'green'],
    'Josh Jung' : (9, 10),
    3 : {0 : 0},
    9000 : 'impale mat a'
  }

  key = find_key(example_dict, 'impale mat a')
  print(key)