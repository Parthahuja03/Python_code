
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







