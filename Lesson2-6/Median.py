# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a, b, c):
    if biggest(a, b, c) == a:
        return bigger(b,c)
    if biggest(a, b, c) == b:
        return bigger(a,c)
    else:
        return bigger(a,b)

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7

#find biggest, then compare the rest of 2, find bigger