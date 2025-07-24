#sets
#data structures
#unordered, dont allow duplicates(removes them)
#can add/remove

'''
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)
'''

#union/intersection/difference

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)

intersec_set = set1.intersection(set2)
print(intersec_set)

diff_set = set1.difference(set2)
print(diff_set)