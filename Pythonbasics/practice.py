#to print the any string
print ("Hello")

# to assign and print multiple variables values in one line
a , b = 2,"great"
print(a ,b)
# to concatenate two variables of same datatype u can use , or + symbol
# using , symbol ----> print (a, b)
#using + symbol
print ( "hello"+ "Wolrd")
#to print two types of datatypes in print statement (eg. string and number)
age=9
print("Hello your age is " ,age)
# to perform calculation inside the double quotes we can use f string
print(f"After 10  years your age will be {age +10}") # output will do the calculation
print("After 10 years your age will be {age+10} years") # if u dont use f string {age+10} will be printed as it is
# we can also perform calculation without using f string
print("your age after 10 years :" ,age + 10)
# to check the data type of the variable we have type() in python
print(type(a))
# you can print string /number along with functions at one separated by commas
print("Age:", age , type(age))
