#LIST
#behaves similar to the array
myList = [1,2,"Parth","Ahuja",3]

#Last two elements-- last index is -1 so consider that and iterate to the last
print(myList[-2:])

#Skipping the alternate number and we can decide the gap between them
print(myList[::2])

#add the elements in the list-- List are mutable(The value can be changed)
myList = [1,2,"Parth","Ahuja",3]
myList.append("Pyhton")
print(myList)

#Delete from end
myList.pop()
print(myList)

#Reverse 
myList.reverse()

#reversed in loop or runtime

my_list =[1,2,3,4,5]
#new_list=[i*i for i in my_list]

new_list=[i*i for i in my_list if (i%2)==0]
print(new_list)


##DICTIONARY-- just like json

myDictionary={"x":1,"y":2,"z":"parth"}
print(myDictionary) #it is also mutable

#Values can be reassigned
myDictionary["x"]=10
print(myDictionary)

myDictionary.pop("z")
print(myDictionary)

print(myDictionary.keys())
print(myDictionary.values())
print(myDictionary.items())


#SETS- to perform mathematical operations
#Remove duplicates in set, only unique values will be there
mySet ={1,2,3,4,4,5,5,5,5}


#Mathematical operations in set
a ={1,2,3,4}
b={3,4,5,6}
print(a.union(b))
print(a.intersection(b))
a.remove(2)
a.add(20)
print(a)

emp ={}
print(type(emp))#Empty is default-Dictionary



#TUPLE-Its a list only
myTuple=(1,2,3,4,5)

#Convert tuple in list
myTupleList=list(myTuple)
myTupleList.append(6)

myTup = tuple(myTupleList)

#LIST AND DICTIONARY IS VERY IMPORTANT
