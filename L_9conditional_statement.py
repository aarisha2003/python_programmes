###################################################################################################################
#not equal
a=10
b=20
print(a==b)# equality operator
print(a!=b)# not eqality operator
print(a<=b)#less than or equal too
print(a>=b)#greater than or equal too
print(a>b and a<b)
print(a<b and a<b) # when both conditions are true than only it will give true otherwise it will give false
print(a>b or a<b)#when both conditions are false than only it will give false otherwise it will give true
print( not a<b)# give oppsite result 
########################################################################################################################
#if
age=int(input('enter your age: '))
if age>= 18 and age<=49:
    print( 'you are eligible for vote')

elif age>= 50:# elif can be use multiple time
    print('eligible and need transporation service also') 

else:
    print(' you are not eligible for vote')  
############################################################################################################    


