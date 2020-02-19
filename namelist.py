namelist1 = ([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'
namelist2 = ([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'
namelist3 = ([ {'name': 'Bart'} ])
# returns 'Bart'
namelist4 = ([])
# returns ''

def namelist(names):
  # if length of names is greater than 1
  if len(names) > 1:
    # interpolate (return) the name['name'] 
    return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name'])
  elif names:
    return names[0]['name']
  else:
    return ''

print namelist(namelist1)
# print namelist(namelist2)
# print namelist(namelist3)
# print namelist(namelist4)