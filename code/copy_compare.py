watches1 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

#print('No copy method')
#print('--------------')

watches2 = watches1

#print(id(watches1))
#print(id(watches2))

#print('\nWith copy method')
#print('----------------')

watches2 = watches1.copy()

#print(id(watches1))
#print(id(watches2))

watches1 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches2 = {
  'Tank' : 'Cartier',
  'Submariner' : 'Rolex',
  'Speedmaster' : 'Omega'
}

#print(watches1 == watches2)

watches1 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches2 = {
  'Tank' : 'Cartier',
  'Submariner' : 'Rolex',
  'Speedmaster' : 'Omega'
}

print(watches1 < watches2)