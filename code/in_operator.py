watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

def kvpair(watches):
  values = watches.values()
  if 'Tank' in watches and 'Cartier' in values:
    return True
  return False

print(kvpair(watches))

