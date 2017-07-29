# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

#Method 1

def split_string(source, splitlist):
    list = []
    string = ''
    for e in source:
        if e not in splitlist:
            string = string + e
        else:
            if string != '':
                list.append(string)
                string = ''
    if string != '':
        list.append(string)
    return list  

#Medthod 2
def delet_string_belongs_to_splitlist(a, b):
    if b != '':
        a.append(b)

def split_string(source, splitlist):
    list = []
    string = ''
    for e in source:
        if e not in splitlist:
            string = string + e
        else:
            delet_string_belongs_to_splitlist(list, string) #call def delet_...
            string = ''
    delet_string_belongs_to_splitlist(list, string)
    return list  


   
   #思路 主队 list 负责收集所有合格的elements，并且把他们加在一起。
   #     分队 string 负责筛选合格的elements，所有需要有2个全局变量 list and string
   # 筛选elements时候 保存合格elements，string + string。 组好了一组就要运到list里面
   # 并且清空string（string =‘’）
   
   #注意1：for loop中string，是string 中每个字母 比如“An Apple" for e in string 
   # e指向的是A,n，A,p.... for loop 中的list of string ['an', 'apple'] e 指向
   # 的是['an'],['apple']

   #注意2 string != '' 只有当string中含splitlist的元素时候，string会被清空
   

    
out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']