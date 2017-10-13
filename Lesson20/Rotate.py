# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.
#method 1
def rotate(letter, n):
    new = ''
    for e in range(0, len(letter)):
        if letter[e] != ' ':
            alpha = shift_n_letters(letter[e], n)
        else:
            alpha = ' '
        new = new + alpha
    return new
#method 2
def rotate(letter, n):
    new = ''
    for alpha in letter:
        if alpha != ' ':
            new_alpha = shift_n_letters(alpha, n)
        else:
            new_alpha = ' '
        new = new + new_alpha
    return new

def shift_n_letters(letter, n):
    return chr((ord(letter) + n - ord('a')) % 26 + ord('a'))



print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
