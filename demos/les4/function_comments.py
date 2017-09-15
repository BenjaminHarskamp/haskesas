# functions
# Demo purposes, may not be well formatted for display reasons
#
# Robert Schrijvers

# Function comments

from math import pi

def sphere_volume(r):
    return (4/3) * pi *  r**3

print('\n ----------- Default help --------------')
print(help(sphere_volume))
print('\n ---------------------------------------')
















def sphere_volume_2(r):
    'Calculates volume using: (4/3) * pi *  r**3'
    return (4/3) * pi *  r**3

print('\n ----------- Simple help help --------------')
print(help(sphere_volume_2))
print('\n ---------------------------------------')












def sphere_volume_3(r):
    """Calculates volume using: (4/3) * pi *  r**3

    arguments:
       r The radius of the sphere (int/float)

    returns:
        the volume (float)

    """

    return (4/3) * pi *  r**3

print('\n ----------- Extended help --------------')
print(help(sphere_volume_3))
print('\n ---------------------------------------')





def som(a):
   return sum(a)

print(som([3,4]))
