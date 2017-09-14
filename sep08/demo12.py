list1 = list('abcde')
print type(list1),list1,hex(id(list1))
list2 = list1
list3 = list1[:]
list4 = list(list1)
print type(list1),list2,hex(id(list2))
list1[0]='$'
print list1,list2,list3,list4