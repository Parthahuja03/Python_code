myList =["orders","products","customers"]

for i in myList:
    #i is the value of iteration of the list
    if(i=="customers"):
        print(myList.index(i))

#very basic
for i in range(1,101):
    print(i)

# nested for loops

for i in myList:
    print(i)
    for x in i:
        print(x)

#Break statement
myList =["orders","products","customers"]
for i in myList:
    print(i)
    if(i=="products"):
        break

#Continue statement
myList =["orders","products","customers"]
for i in myList:    
    if(i=="products"):
        continue
    #After that the loop code will not work and go in the next Iterations
    print(i)




#--WHILE LOOPS
x=1 #starting point

while(x<11): #ending point
    print(x)
    x=x+1



