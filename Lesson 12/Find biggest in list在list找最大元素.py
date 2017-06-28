Find biggest in list在list找最大元素
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers！！, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(a):
    i = 0
    for e in a:
        if e > i:
            i = e
    return i 




print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0
