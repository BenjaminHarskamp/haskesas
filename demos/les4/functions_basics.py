# functions
# Demo purposes, may not be well formatted for display reasons
#
# Robert Schrijvers

# Basic functions

def multilply_2_by_2():
    a = 2*2
    return a;

# assign the result
var = multilply_2_by_2()
print('multilply_2_by_2() returns: ',var)



















def multilply_by_2(x):
    return x * 2;

















# use it with 1 parameter
print('\nmultilply_by_2(6) returns: ',multilply_by_2(6))














def multilply_by_4(x):
    return x * 4;

print('multilply_by_4(6) returns: ',multilply_by_4(6))


















# use 2 parameters
def multilply(x,y):
    return x * y;

print('\nmultilply(6,2) returns: ',multilply(6,2))
print('multilply(6,4) returns: ',multilply(6,4))


m = 4
print('\nCall function in a loop')
# use in a loop with a range
for x in range(11):
    print('multilply({0},{1}) returns: {2}'.format(x,m,multilply(x,m)))













from math import pi

def sphere_area(r):
    return 4 * pi * r**2


def sphere_volume(r):
    return (4/3) * pi *  r**3

print('\nArea and volume of a sphere')
# use in a loop with a range
for r in range(1,11):
    print('{0:5.2f}{1:10.2f}{2:10.2f}'.format(r,sphere_area(r),sphere_volume(r)))
