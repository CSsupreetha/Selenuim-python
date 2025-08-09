# to print integer , string and float
a,b,c=10,3.4,"hello"
print(a,b,c)
# to take the input from the user u have to use input() function
#if u want to take a string as input
a=input("Enter your name")
print(a)
#python takes inputs as string by default , hence its imp to convert the numeric input into integer using int() if u want to perform any numerica operations or comparision
b=input("Enter your age")
print(b , type(b)) # this works but it takes b as string
# list : It is a  collection of items that can be of any dattype , including strings, integers, floats, and other lists
# List is ordered , mutable and indexed
# you can create a list using square brackets []
v=[2, 4, 6.1, 8, "hello" , "world"]
print(v , type(v))
# to access and print the items in list
print(v[3]) #prints the item present in the location 3
#We can perform manupulation operations on list such as insertion, append, updation and deletion
# to insert the items into the list- it adds the item into to specified location
v.insert(3, "Hai") # 3 is location and "hai " is the valuse u want to insert , output : [2, 4, 6.1, "Hai",8, "hello" , "world"]
print(v)
#to append , it add the item at the end of the list
v.append("Welcome")
#to update the values in list
v[6]="Students" # replaces world with Students
#to delete the item from list
del  v[3]
print(v)

#tuple - sequence of orderd items , but they are immutable created using () seperated by ,
t=(5, 6, "good", "kind")
print(t)
t[3]=7 # u cannot update the tuple items
print(t)
# common tuple operation include indexing ,slicing, concatenation
# idexing - accessing and printing the tuple items
print([t[2]])
#slicing - to extracting a subset of tuple
print(t[1:4]) # prints the items from the location 1 to 3 , excludes 4 th location
# concatination  - combining tow tuples using '+' operator
t1=("hello" , "Students")
t2 = ("Welcome " , "to" , "Python class")
print(t1 + t2)
# u can repeate the tuples multiple times using * operator
print(t1 *2) # ptints tuples t1 2 times output: hello students hello students
# activity  on list

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("First fruit:",fruits[0] )
print("Last fruit:", fruits[4] )
print("Fruits from index 1 to 2:", fruits[1:3])

#Dictionary
car={"make": "Toyota" , "model" : "Camry" , "year":2020, "color" : "Blue"}
print(car["model"])
car["owner"]="Rahul"
print(car)

