set1 = {'P','I','N','E','A','P','P','L','E'}
set2 = {'B','A','N','A','N','A'}
print set1,set2

set3 = set1 | set2
print set3

set4 = set1 & set2
print set4

set5 = set1 ^ set2
print set5

set6 = set4 | set5
print set6
print set3 == set6

set7 ={'A','N','L'}
print set7<set2
print set7<set1
print set1-set7,set2-set7

print len(set1)