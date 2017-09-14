class Person:
    def __init__(self,age):
        self.age = age

age=38
print 'when age=38,age id=%s'% hex(id(age))
age=39
print 'after age=39,age id=%s'% hex(id(age))
person1 = Person(38)
addr1 = hex(id(person1))
addr2 = hex(id(person1.age))
print ('person id=%s,person.age id=%s')%(addr1,addr2)
person1.age=39
addr1 = hex(id(person1))
addr2 = hex(id(person1.age))
print ('person id=%s,person.age id=%s')%(addr1,addr2)