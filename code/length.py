watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

#print(len(watches))

watches = {}

#print(len(watches))

def pop_item(d):
  if len(d) == 0:
    return -1
  return d.popitem()  
watches = {}
print(pop_item(watches))