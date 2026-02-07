
#parameters 
def myFun(x):
    if (x>10):
        print("Greater than 10")
    else:
        print("less than 10")
    return x
#default value
def myFun2(x=30):
    if (x>10):
        print("Greater than 10")
    else:
        print("less than 10")
    return x

myFun(20)
myFun(2)


#multiple input
def myFun2(*x):
    print(x)

myFun2(20,30,40)



def myFun2(**x):
    print(x)

myFun2(a=20,b=30,c=40)


#LAMDA Functions

#--normal function
def add(x,y):
    print(x+y)

add(2,3)

#-- lamda function-- only for light weight functions

add = lambda x, y : x+y
print(add(2,3))

#MAP_FILTER_REDUCE

myList =[1,2,3,4,5]

def square(p_x):
    ret_list =[i*i for i in p_x]
    print(ret_list)
    
square(myList)

#Map
myList =[1,2,3,4,5]
def squareInd(p_x):
    return p_x*p_x

result = list(map(squareInd,myList))#- map each item of myList and passing it in square function
print(result)

#Filter
myList =[1,2,3,4,5]
def square(p_x):
    if(p_x%2==0):
        return p_x*p_x #- in that case , none will be printed as it is not filtering out the odd cases

result = list(map(square,myList))#- in that case , none will be printed as it is not filtering out the odd cases

result2 = list(filter(square,myList))
print(result)
print(result2)

#Reduce

from functools import reduce # This is not default imported , we need to import it in every piece of code

myList =[1,2,3,4,5]
def squareInd(p_x,p_y):
    return p_x*p_y
result = reduce(squareInd,myList)
print(result)


#fString
name="Parth"
# Just by putting f before the "", it will take the variable into the string
print(f"my name is {name}")


#Custom error and exception 

x=99

if(x<100):
    raise ValueError("value< 100 is not allowed")

if(x<100):
    raise Exception("value< 100 is not allowed")


#enumerate

myList =[10,20,30,40]
for i in enumerate (myList):
    print(i)
for i,x in enumerate(myList):
    print(x)






