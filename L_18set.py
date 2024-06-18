my_set={'pen','pencile','earser'}
print(my_set)
# sets are unordered so you cann't we sure in which order the item will appear.
my_set1={'pen','pencile','earser','pen','pencile'}
print( my_set1)
# set will not allow duplicate values it only give unique value of the item.
# unchangeable=it means it cann't change the item after the set has been created .
# once set is created you cann't change the item but you can remove  and add a item.
my_set2={'pen','pencile','earser','pen','pencile',1,2}
print(my_set2)
# you cannt acess a item in a set by refering a index or a key 
# print(my_set2[2])
for i in my_set2:
    print(i)

print('pen'in my_set2) 
print('pen'not in  my_set2) 
# two member opertor in and not member
my_set3={'table','chair'}
my_set2.add('paint')
print(my_set2)
my_set2.update(my_set3)
print(my_set2)