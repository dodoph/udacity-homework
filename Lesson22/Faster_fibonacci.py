#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    a = 0
    b = 1
    for n in range(0, n):
        c = a + b
        a = b
        b = c
    return a

def fibonacci(n):
    a = 0
    b = 1
    for n in range(0, n):
        a, b = b, a + b
#n = 0 range(0,0) = [], does not entry the for loop so n = 0 return a = 0
print fibonacci(0)
#>>> 14930352
