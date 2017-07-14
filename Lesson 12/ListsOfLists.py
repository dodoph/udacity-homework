# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(p):
    total_numbers = 0
    total_tuitions = 0
    for name, numbers, tuitions in p:
        total_numbers = total_numbers + numbers
        total_tuitions = total_tuitions +  numbers * tuitions
    return total_numbers, total_tuitions

def total_enrollment(p):
    total_numbers = 0
    total_tuitions = 0
    for e in p:
        total_numbers = total_numbers + e[1]
        total_tuitions = total_tuitions +  e[1] * e[2]
    return total_numbers, total_tuitions





print total_enrollment(udacious_univs)
#>>> (90000,0)

# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside 
# interpreter you might not see it.

print total_enrollment(usa_univs)
#>>> (77285,3058581079)


# 1.确定需要return是什么
# 2.
# 因为是需要不断把上面一个数值累积。return得到的是一个total。初始时候，从上面累积下来是0，什么也没有。所以，要定义一个初始值（0）。f
# or e in p 中，e是每次需要从每一个list抓取出来的。是一个变量！
# 3. e 是一个list 里面可以是很多元素，这些元素也是可以为lists，（lists of lists）所以在for e in p
# 里面可以用 list of list 中几个元素表示

