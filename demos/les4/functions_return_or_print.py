# functions
# Demo purposes, may not be well formatted for display reasons
#
# Robert Schrijvers

# return or print




# use 2 parameters, return result
def multilply(x,y):
    return x * y;


# use 2 parameters, print result
def multilply_show(x,y):
    print ("in de functie", x * y);


result1 = multilply(6,3)
result2 = multilply_show(5,4)

print('result1',result1,type(result1))
print('result2',result2,type(result2))









print('\n\n')






def print_info(var,txt):
    print(txt,var,type(var))


print_info(multilply(6,3),'multilply(6,3) =')
print_info(multilply_show(5,4),'multilply_show(5,4) =')



















