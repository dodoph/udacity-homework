# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number


def numbers_in_lists(string):
    sublist = []
    result = []
    result.append(int(string[0]))
    notinsublist = True
    n = 0
    for e in string[:-1]:
        e = int(e)
        if e > int(string[n+1]):
            if notinsublist:
                sublist = []
                result.append(sublist)
            sublist.append(int(string[n+1]))
            notinsublist = False
        else:
            result.append(int(string[n+1]))
            notinsublist = True
        n = n + 1
    return result

    