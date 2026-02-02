#String act as an array
name ="parth"
print(name[0])

#slicing
print(name[0:3])  # 3rd index is not included
print(name[:])  #auto from 0 to n (length)
print(name[0:len(name)])


#String Methods
print(name.upper())
print(name.lower())
print(name.capitalize())

#Replace method
replaced_name = name.replace("th","ishi")
print(replaced_name)



#--Split function
toSplit = "Parth Sanjeev Ahuja"
myList = toSplit.split(" ")
print(myList)

#Ends with / Starts With

file="raw_data.csv"
if(file.endswith(".csv")):
    print("csv file")

if(file.startswith("raw")):
    print("This is a raw file")

#count the occurence
statement ="Hello my  name is parth and parth is studying python right now"
print(statement.count("parth"))
print(statement.count("is"))

#Check the data Type
demoStr = "Hello"
demoVar=10
demoVar2="10"

print(demoStr.isnumeric())
#print(demoVar.isnumeric()) #-- Works only in the case of string
print(demoVar2.isnumeric())

#Explore more methods by your own