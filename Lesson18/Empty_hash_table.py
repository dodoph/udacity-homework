# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

#method 1 while loop
def make_hashtable(nbuckets):
    index = []
    number = 0
    while number < nbuckets:
        index.append([])
        number = number + 1
    return index
#method 2 for range loop
def make_hashtable(nbuckets):
    index = []
    for e in range(0, nbuckets):
        index.append([])
    return index

print make_hashtable(4)
