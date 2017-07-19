list1 = [1,2,3,4]
list2 = [1,2,3,4]
list1 = list1 + [5,6]
list2 = append([5,6])

print list1 
#>>>[1,2,3,4,5,6]
print list2 
#>>>[1,2,3,4,[5,6]]
list1 += ['a',4]
print list1
#>>>[1,2,3,4,'a',4]

