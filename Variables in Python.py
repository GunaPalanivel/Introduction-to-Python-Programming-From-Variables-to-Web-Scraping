#!/usr/bin/env python
# coding: utf-8

# In[1]:


#WHAT DO VARIABLES MEAN? 


#Variables are entities of a program that hold a value like X=200.

#To understand this better 
 #[ The box is holding a value. A variable would be the name given to the box]

#X would be the variable name and 200 would be the value of the variable.

#As we'll go through the various topics here, 
 #you'll have the better understanding why we use and how to use them.

    
#VARIOUS DATA TYPES OF VARIABLES. 
#LET ME EXPLAIN WHAT DATA TYPES ARE.


#WHAT DO DATA TYPES MEAN?  


#The type of value that you assign to the variables.

#There are two types of numbers Integers and Float.

#Integers means numbers without a decimal point.

#Float means numbers with a decimal point.

#Other than this a Common data type is String. 

#Sting means a collection of characters [any words]


# In[2]:


#In this code snippet, 
 #we declare a variable X and assign it the value of 100.
    
#The next line of code type(X) is used to determine the type of X. 
 #In this case, X is an integer, so running this line of code will output <class 'int'>.

#The type() function is a built-in Python function that returns the type of the object passed to it.

#In this case, we passed the variable X to the type() function, 
 #and it returned the type of X, which is int.

#This code is a simple example of how to use Python variables and the type() function to determine the type of a variable.

#By assigning a value to a variable, we can store data in memory and manipulate it in our code.

#The type() function is a useful tool for debugging and verifying the type of data in our code.


X = 200
type(X)


# In[3]:


#We declare a variable X and assign it the result of the arithmetic operation 648*789. 
 #When this line of code is executed, Python multiplies 648 and 789, and assigns the result to X. 
   #In this case, X has a value of 512472.

#The next line of code type(X) is used to determine the type of X. In this case, X is an integer, 
 #so running this line of code will output <class 'int'>.

#The type() function is a built-in Python function that returns the type of the object passed to it. In this case, 
 #we passed the variable X to the type() function, and it returned the type of X, which is int.


X = 648*789
type(X)


# In[4]:


#We declare a variable X and assign it the result of the arithmetic operation 648*789. When this line of code is executed, 
 #Python multiplies 648 and 789, and assigns the result to X. In this case, X has a value of 512472.

#The print() function is then used to output the value of X to the console. When this line of code is executed, 
 #Python prints the value of X to the console, which in this case is 512472.


X = 648*789
print(X)


# In[5]:


#we declare a variable X and assign it the value 3.254. This value is a decimal or a floating-point number. 
 #When this line of code is executed, Python assigns the value 3.254 to X.

#The next line of code type(X) is used to determine the type of X. In this case, X is a floating-point number, 
 #so running this line of code will output <class 'float'>.

#The type() function is a built-in Python function that returns the type of the object passed to it. 
 #In this case, we passed the variable X to the type() function, and it returned the type of X, which is float.


X = 3.254
type(X)


# In[6]:


#We declare a variable X and assign it the string value "Python". 
 #The print() function is then used to output the value of X to the console. When this line of code is executed, 
   #the string "Python" will be printed to the console.

#In Python, we can use single or double quotes to create string literals. In this case, we used double quotes, 
 #but single quotes would also work. The print() function is a built-in Python function that outputs data to the console. 
   #When we pass the variable X as an argument to print(), it will output the value of X to the console.


X = "Python"
print(X)


# In[7]:


#In the first line of code, we declare a variable X and assign it a string value of "Python" using double quotes. 
 #Double quotes and single quotes are both used to declare string literals in Python, 
    #and in this case, the string is enclosed in double quotes.

#In the second line of code, we declare a variable X and assign it a string value of "Python" using single quotes. 
 #Again, single quotes and double quotes can be used interchangeably to declare strings in Python.

#The third line of code print(X) is used to print the value of X to the console. 
 #Since the value of X is the same in both lines of code, 
    #running this line of code after either line will output the string "Python".

#The type(X) function is used in the first line of code to determine the type of X. In this case, X is a string, 
 #so running this line of code will output <class 'str'>.

#The main difference between the two lines of code is the type of quotes used to enclose the string value. 
 #While both double quotes and single quotes can be used to declare strings in Python, 
    #it's important to be consistent in your usage throughout your code.


X = 'Python'
print(X)


# In[8]:


#We declare a variable X and assign it a string value of "Python". When this line of code is executed, 
 #Python creates a string object with the value "Python", and assigns it to the variable X.

#The next line of code type(X) is used to determine the type of X. In this case, X is a string, 
 #so running this line of code will output <class 'str'>.


X = "Python"
type(X)


# In[9]:


#A tuple is an immutable series of components that is ordered in Python.
 #This implies that a tuple's contents cannot be modified once it has been constructed. 
    #Tuples can include items of any data type, including other tuples, and are denoted by parenthesis ().

#IN THAT THEY MAY HOLD NUMEROUS ELEMENTS, TUPLES AND LISTS ARE SIMILAR, BUT THERE ARE A FEW KEY DISTINCTIONS:

#Tuples are immutable, whereas lists are changeable, meaning that their contents can be altered after they are generated.

#Square brackets [] are used to denote lists, and parentheses are used to denote tuples ().

#Tuples are used when we need to keep a collection of objects that shouldn't be modified after they are generated, 
 #while lists are often used when we need to store a collection of items that can be modified over time.

#Ultimately, 
 #Python tuples can be a valuable tool for storing collections of data that shouldn't be modified after they are produced. 
   #Writing efficient Python code requires a grasp of the distinctions between tuples and lists.


# In[10]:


#LIST


# In[11]:


#A list is a type of data structure in Python that lets you store a group of elements. It is a changeable object, 
 #so after you construct the list, you can change, add, or remove elements. 
    #Lists are made by enclosing the elements in square brackets [] and using commas to separate them.


# In[12]:


#X is a variable that is declared, and we give it a list of three integer values, 
 #namely 18, 58, and 48. The list is defined by the square brackets [], and commas are used to separate the values.

#The contents of X are then written to the console using the print() function. 
 #Python will show the list [18, 58, 48] in the console when this line of code is executed.

#One of the most used data structures in Python is the list. 
 #They are employed to keep an assortment of values that can be accessed and changed in different ways.

X = [18,58,48]
print(X)


# In[13]:


#we declare a variable called X and give it a list of the three integer numbers 18, 58, and 48. 
 #An ordered group of variables is referred to as a list in Python.

#To find out what type of X it is, use the type(X) command in the following line of code. 
 #The output of this piece of code, since X in this case is a list, is class 'list'>.

#The type of the object it was supplied as a parameter is returned by the built-in Python method type(). 
 #In this instance, we used the type() method and supplied the variable X. Its type, which is list, was returned.


X = [18,58,48]
type(X)


# In[14]:


#Declaring the variable X, we give it a list with the elements 18, 58, and 48 in it. 
 #The elements in the list are separated by commas and are enclosed in square brackets []. 
    #Because it solely contains numbers, this kind of list is known as a numeric list.

#The first entry of the list X, which has an index of 0, is accessed in the following line of code print(X[0]). 
 #The first element of the list has an index of 0, the second element has an index of 1, 
    #and so on since list indices in Python start at 0. With the print() function, 
       #we can output the value of the list's first element's index to the console.

#In this instance, since 18 is the value of the list's first member, running this line of code will output 18 to the console.


X = [18,58,48]
print(X[0])


# In[15]:


#we create the list variable X and give it the array of numbers [18, 58, 48]. 
 #Python lists are used to hold collections of objects, 
    #including texts, numbers, and other types of data.

#The third item in the list X, which has an index of 2, is printed in the next line of code, print(X[2]). 
 #The first item in the list has an index of 0 since list indexing in Python starts at 0, the second item has an index of 1, 
    #and so on. We use an index of 2 because we want to publish the third item in the list.

#The value 48 is reported to the console when this line of code is run.

X = [18,58,48]
print(X[2])


# In[16]:


#Three integer values—18, 58, and 48—are created in the list X by this code. 
 #The values for the list are enclosed in square brackets and separated by commas.

#X[1] = 20 is the next line of code. the list's second member (located at index 1) now has the value 20. 
 #The second entry of the list has an index of 1, since list indices in Python begin at 0.

#Once the update has been made, the list's contents are shown using the print(X) function. The result will reveal that, 
 #although the other elements stay unchanged, the second element (located at index 1) has changed from 58 to 20.

#This code shows how to construct a list in Python, access and alter list elements, 
 #and display the list's contents using the print() function.


X = [18,58,48]
X[1] = 20
print(X)


# In[17]:


#TUPLE


# In[18]:


#A tuple is an immutable series of components that is ordered in Python. 
 #This implies that a tuple's contents cannot be modified once it has been constructed. 
    #Tuples can include items of any data type, including other tuples, and are denoted by parenthesis ().

#Tuples are more effective than lists at storing and accessing elements, which is one of their key advantages. 
 #This is because lists are stored in a fragmented block of memory that must be resized when elements are added or removed, 
    #whereas tuples are maintained in a contiguous block of memory.

#IN THAT THEY MAY HOLD NUMEROUS ELEMENTS, TUPLES AND LISTS ARE SIMILAR, BUT THERE ARE A FEW KEY DISTINCTIONS:

#Tuples are immutable, whereas lists are changeable, meaning that their contents can be altered after they are generated.

#Square brackets [] are used to denote lists, and parentheses are used to denote tuples ().

#Tuples are used when we need to keep a collection of objects that shouldn't be modified after they are generated, 
 #while lists are often used when we need to store a collection of items that can be modified over time.

#Overall, Python's tuples feature can be beneficial for storing data sets that shouldn't be altered once they are produced.


# In[19]:


#Declaring a variable called X, we assign it a tuple consisting of the numbers 2, 5, 8, and 6. 
 #A Python data structure called a tuple allows many values of various types to be stored in a single variable. 
    #Tuples are immutable, thus once their values have been assigned, they cannot be modified.

#The contents of X are sent to the console using the next line of code, print(X). 
 #Python will output (2, 5, 8, 6) to the console when this line of code is run.

#This example explains how to use tuples in Python 
 #to store many values in a single variable by defining a variable and assigning it a tuple of values. 
    #The tuple's contents are shown on the console using the print() function.


X = (2,5,8,6)
print(X)


# In[20]:


#X is a variable that we define, and we give it a tuple of four components (2,5,8,6). 
 #A tuple is an immutable collection of ordered components that is similar to a list 
    #in that its elements cannot be modified after it has been constructed.

#The type of X is determined by the next line of code, type(X). 
 #Python executes this line of code and returns the type of X, which is class 'tuple'>.

#The type of the object provided to the built-in Python type() method is returned. 
 #In this instance, the type() method took the variable X as a parameter and returned the tuple type.

X = (2,5,8,6)
type(X)


# In[21]:


#we create a variable called X and assign a tuple to it (2, 5, 8, 6). Similar to a list in Python, 
 #a tuple is an ordered collection of things that cannot be changed after it has been generated.

#The code that follows The third element of the tuple is produced by the print() function using the syntax print(X[2]). 
 #As indexes in Python begin at 0, X[2] refers to the tuple's third component, which has the value 8. As a result, 
    #when this line of code is executed, 8 is produced.

#This example shows how to generate a tuple in Python and how to use index notation to access the items in the tuple. 
 #We can print the value of a particular item in the tuple to the console by using the print() function.


X = X = (2,5,8,6)
print(X[2])


# In[22]:


#we create a variable called X and assign a tuple to it (2, 5, 8, 6). A tuple is an ordered group of objects that, 
 #as was previously noted, cannot be changed after it has been constructed.

#The second item in the tuple is modified to a new value of 20 in the next line of code, X[1] = 20. 
 #The operation will fail with a TypeError 
    #and a warning stating that the "tuple" object does not support item assignment since tuples are immutable in Python.

#Print(X) tries to send the changed tuple to the console in the final step. This line of code won't run, though, 
 #because the previous one raised an error.

#This example demonstrates how Python handles immutable data structures like tuples, 
 #and how attempting to modify them can lead to errors. 
    #It also shows how Python's error messages can provide helpful information in diagnosing the source of the problem.


X = X = (2,5,8,6)
X[1] = 20
print(X)


# In[23]:


#This program uses tuple unpacking to assign the values 4, 5, and 7 to the variables x, y, and z, respectively. 
 #The values of x, y, and z are then printed; they are 4, 5, and 7 respectively.

#When working with functions that return multiple values or when working with tuples in general, 
 #this example shows how to use tuple unpacking to assign multiple variables in a single line of code. 
    #Additionally, it demonstrates how to write a code block that prints multiple variables.


(x,y,z) = 4,5,7
print(x)
print(y)
print(z)


# In[24]:


#Print(x,y,z) and (x,y,z) = 4,5,7 both use the Python tuple unpacking syntax, but their functions are distinct from one another.

#The first line of code uses tuple unpacking to give the variables x, y, and z, respectively, the values 4, 5, and 7. 
 #This is a quick way to give different values to various variables on the same line. 
    #The values are assigned to the variables in the tuple's order of appearance.

#The values of the variables x, y, and z are printed on the same line and are separated by spaces in the second code, 
 #print(x,y,z). This eliminates the need to print each variable's value on a separate line 
    #and allows the values of multiple variables to be displayed simultaneously.

#The primary distinction between the two code snippets is in the way they accomplish their goals: 
 #the first assigns values to variables, while the second prints those values to the console.



(x,y,z) = 4,5,7
print(x,y,z)


# In[25]:


#Because the number of values on the right side of the equal sign (3) does not match the number of variables on the left side, 
 #the code (x,y) = 4,5,7 will produce a ValueError (2).

#The number of values and variables must coincide in order to assign values to multiple variables in a single line. 
 #For instance, (x, Y, Z) = 4,5,7 gives the values 4 to X, Y, and Z, respectively.

#With commas separating the values, 
 #multiple variables in Python can have their values set simultaneously using a single line of code. 
    #There are three values (4, 5, 7) in the code (x,y) = 4,5,7, but there are only two variables (x and y) to assign them to. 
       #The ValueError is the outcome of this.

#In conclusion, the code (x,y) = 4,5,7 will produce an error because the number of variables on the left side 
 #and the number of values on the right side of the equal sign do not match. 
    #The proper way to assign values to multiple variables in Python is to use the same number of variables and values separated by commas.


(x,y) = 4,5,7


# In[26]:


(x,y,z) = 2,2,2
print(x,y,z)


#Tuple unpacking is used in the code (x,y,z) = 2,2,2 to assign the values 2,2,2 to the variables x, y, and z, respectively. 
 #Then, using print, we are printing these variables (x,y,z). The result will be 2 2 2.

#All three variables, x, y, and z, are given the value 1 in a single line of code, x = y = z = 1. 
 #When multiple variables are assigned the same value in a single statement, this is referred to as chained assignment. 
    #Then, using print, we are printing these variables (x,y,z). The result will be 1 1 1.

#The way the variables are assigned values thus represents the primary distinction. 
 #While chained assignment is used in the second code to assign values, 
    #tuple unpacking is used to assign values in the first code.


x = y = z = 1
print(x,y,z)


# In[27]:


#Requirements for variable naming.


# In[28]:


#WRITING READABLE AND MAINTAINABLE CODE IN PYTHON REQUIRES PROPER VARIABLE NAMING. VARIABLE NAMING TYPICALLY ADHERES TO THE FOLLOWING RULES:

#Variables ought to have a letter or an underscore at the beginning.

#Variables ought to have a letter or an underscore at the beginning.

#Letters, numbers, and underscores are all permitted in variable names.

#Letters, numbers, and underscores are all permitted in variable names.

#Name and Name are two different variables because variable names are case-sensitive.

#Name and Name are two different variables because variable names are case-sensitive.

#To make the purpose of a variable clear to other programmers, variables should have descriptive and meaningful names.

#As variable names, stay away from using reserved words. For instance, in Python, reserved words like if, else, while, for, etc.
 #cannot be used as variable names.

#In most cases, variable names should be written in lowercase. For constants, capitalize all letters (values that do not change).

#Use underscores to divide words in a variable name that has multiple words. First name or my variable name, for instance.

#THESE RECOMMENDATIONS WILL MAKE YOUR CODE EASIER TO READ AND COMPREHEND FOR OTHER PROGRAMMERS, 
 #WHICH IS CRUCIAL FOR TEAM PROJECTS AND LONG-TERM CODE MAINTENANCE.


# In[29]:


#Principle 1.
#Names of variables must start with an alphabet character or an underscore ( ).
#Like abc and _abc rather than 5abc and %abc.


# In[30]:


abc = 234
print(abc)


# In[31]:


_abc = 234
print(_abc)


# In[32]:


7abc = 234
print(7abc)


# In[33]:


&abc = 234
print(&abc)


# In[34]:


#Principle 2.
#Alphabets, numerals, or an underscore can come after the first character.
#Like a102 and a342, not a589 and xyz-4.


# In[35]:


a102 = 75
print(a102)


# In[36]:


_a342_ = 75
print(_a342_)


# In[37]:


a589$ = 75
print(a589$)


# In[38]:


xyz-4 = 75
print(xyz-4)


# In[39]:


#Principle 3.
#Names of variables are case sensitive.
#A250 is not the same as #a250.


# In[40]:


a250 = 34
A250 = 56
print(a250)
print(A250)


# In[41]:


a250 = 34
A250 = 56
b250 = 78
print(a250, b250, A250)


# In[42]:


a250 = 34
A250 = 56
b250 = 78
print(a250, A250, b250)


# In[43]:


#Principle 4.
#Reserved terms, such as break, class, try, and all others, cannot be used as variable names.


# In[44]:


break = 56
print(break)


# In[45]:


try = 56
type(try)


# In[46]:


#35 RESERVED KEYWORDS IN PYTHON HAVE PREDETERMINED MEANINGS AND ARE NOT PERMITTED TO BE USED AS VARIABLE NAMES OR IDENTIFIERS. 
 #THE COMPLETE LIST OF PYTHON'S RESERVED KEYWORDS IS PROVIDED BELOW:

#False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, 
 #global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield.


# In[47]:


#Arithmetic Operators


# In[48]:


#ONE OF THE FUNDAMENTAL IDEAS IN PROGRAMMING IS THE CONCEPT OF ARITHMETIC OPERATIONS. 
 #TO PERFORM ARITHMETIC OPERATIONS ON NUMERIC DATA TYPES, PYTHON OFFERS A VARIETY OF ARITHMETIC OPERATORS. 
    #THE ARITHMETIC OPERATORS IN PYTHON ARE AS FOLLOWS:
    
#+: Adds two operands in addition.

#Addition (+): Adds the first operand to the second operand.

#Adding two operands together multiplies them (*).

#Division (/): Divides the first and second operands by one.

#Divides the first operand by the second operand and returns the quotient (floor division, /).

#Modulus (%): Returns the remainder after dividing the first operand by the second operand.

#Raising the first operand to the power of the second operand is known as exponentiation (**).    


# In[49]:


#It's important to remember that only numeric data types, like integers, floats, and complex numbers, 
 #can be used for arithmetic operations. When performing multiple arithmetic operations in a single statement, 
    #the precedence of operators must also be taken into account. The following is the order of precedence:

#Parentheses
#Exponentiation
#Modulus, Division, Floor Division, and Multiplication (evaluated from left to right)
#Subtraction and Addition (evaluated from left to right)

#It's crucial to pick a name for variables used in arithmetic operations that accurately describes the information being stored there. 
 #The Python naming conventions should be followed, and variable names should be clear and concise. 
    #For instance, variable names must not contain spaces or special characters and must begin with a letter or an underscore. 
       #Using lowercase letters for variable names is also recommended, with the exception of constants, which should be written in uppercase.


# In[50]:


#Addition (+): Adds the first operand to the second operand.


x = 4
y = 9
result = x+y
print(result)


# In[51]:


#Subtraction (-): Subtracts the first operand to the second operand.


x = 4
y = 9
result = x-y
print(result)


# In[52]:


#Adding two operands together multiplies them (*).


x = 4
y = 9
result = x*y
print(result)


# In[53]:


#Division (/): Divides the first and second operands by one.


x = 4
y = 9
result = x/y
print(result)


# In[54]:


#Divides the first operand by the second operand and returns the quotient (floor division, /).


x = 4
y = 9
result = x//y
print(result)


# In[55]:


#In this code, the variables x and y are declared, and their respective values are 4 and 9, respectively. 
 #Then we perform exponentiation, or x raised to the power of y, using the double-asterisk ** operator. 
    #The variable result is then given the outcome of this operation. We then print the value of the result.

#In this case, x raised to the power of y is equal to 4, which is a very big number, raised to the power of 9. 
 #This code demonstrates how to raise one value to the power of another using exponentiation in Python using the ** operator.


x = 4
y = 9
result = x**y
print(result)


# In[56]:


#Division (/): Divides the first and second operands by one.


x = 4
y = 2
result = x/y
print(result)


# In[57]:


#Divides the first operand by the second operand and returns the quotient (floor division, /).


x = 4
y = 9
result = x//y
print(result)


# In[58]:


#Modulus (%): Returns the remainder after dividing the first operand by the second operand.


x = 4
y = 9
result = x%y
print(result)


# In[59]:


#Division (/): Divides the first and second operands by one.


x = 4.47
y = 9.76
result = x/y
print(result)


# In[60]:


#String Operations


# In[61]:


#STRINGS ARE COLLECTIONS OF CHARACTERS THAT ARE ENCASED IN QUOTES IN PYTHON. 
 #THE TERM "STRING OPERATIONS" REFERS TO A VARIETY OF TECHNIQUES THAT CAN BE USED TO MANIPULATE AND TRANSFORM STRINGS. 
    #IN PYTHON, A FEW OF THE MOST POPULAR STRING OPERATIONS ARE AS FOLLOWS:

#Concatenation entails using the "+" operator to join two or more strings together. 
 #For instance, the string "helloworld" would be produced by adding "hello" and "world."

#Accessing individual characters in a string by using their location within it is called indexing. 
 #For instance, the index notation "hello[0]" can be used to access the first character in the string "hello".

#Slicing: Using the starting and ending indices of a string, a portion of the string is extracted. 
 #For instance, the notation "hello[1:4]" can be used to slice the string "hello" to get the substring "ell".

#Length: The "len()" function is used to determine how many characters are present in a string. 
 #For instance, the command "len('hello')" would return the value 5 when used to determine the length of the string.

#Formatting: Using the "" notation, a string is modified to include dynamic values.
 #For instance, the command "print('Hello,!'.format('John'))" can format "Hello,! " to include the name "John".

#Case conversion entails using the ".upper()" and ".lower()" methods to change a string's case to uppercase or lowercase. 
 #For instance, the command "print('Hello'.lower())" will return the value "hello" if the string "Hello" is converted to lowercase.

#THESE ARE JUST A FEW OF THE NUMEROUS STRING OPERATIONS PYTHON OFFERS. 
 #EFFECTIVE STRING MANIPULATION IN PYTHON PROGRAMMING REQUIRES AN UNDERSTANDING OF THESE OPERATIONS.


# In[62]:


#Concatenation entails using the "+" operator to join two or more strings together. 
 #For instance, the string "helloworld" would be produced by adding "hello" and "world."


var1 = "Hello"
var2 = "world"
concatenated = var1 + " " + var2
print(concatenated)


# In[63]:


#Accessing individual characters in a string by using their location within it is called indexing. 
 #For instance, the index notation "hello[0]" can be used to access the first character in the string "hello".


var1 = "Hello"
var2 = "world"
print(var1[1])
print(var2[-1]) 


# In[64]:


#Slicing: Using the starting and ending indices of a string, a portion of the string is extracted. 
 #For instance, the notation "hello[1:4]" can be used to slice the string "hello" to get the substring "ell".


var1 = "Hello"
var2 = "world"
print(var1[1:4]) 
print(var2[2:]) 


# In[65]:


#Length: The "len()" function is used to determine how many characters are present in a string. 
 #For instance, the command "len('hello')" would return the value 5 when used to determine the length of the string.


var1 = "Hello"
var2 = "world"
print(len(var1))
print(len(var2))


# In[66]:


#Formatting: Using the "" notation, a string is modified to include dynamic values. 
 #For instance, the command "print('Hello,!'.format('John'))" can format "Hello,! " to include the name "John".


var1 = "Hello"
var2 = "world"
formatted = "{} {}!".format(var1, var2)
print(formatted)


var1 = "hello"
formatted = "I say {}!".format(var1)
print(formatted)


# In[67]:


#Case conversion entails using the ".upper()" and ".lower()" methods to change a string's case to uppercase or lowercase. 
 #For instance, the command "print('Hello'.lower())" will return the value "hello" if the string "Hello" is converted to lowercase.


var1 = "Hello"
lowercase = var1.lower()
uppercase = var1.upper()
print(lowercase) 
print(uppercase)


var1 = "Hello"
var2 = "world"
print(var1.lower()) # Output: "hello"
print(var2.upper()) # Output: "WORLD"


# In[68]:


var = "python"
type(var)


# In[69]:


#Variable "python" is used (var[0]) - This program prints the letter "p," the first character in the string "python." 
 #Since indexing in Python begins at 0, var[0] returns the string's first character.


var = "python"
print(var[0])


# In[70]:


#Variable "python" is used (var[5]) - The sixth character of the string "python," which is the letter "n," is printed by this program. 
 #Again, indexing begins at 0, so var[5] returns the string's sixth character.


var = "python"
print(var[5])


# In[71]:


#Variable "python" is used (var[0:1]) - This program prints the "python" substring starting at character 1 and ending at character 2, 
#in that order (exclusive). As a result, the string "p" is printed.


var = "python"
print(var[0:1])


# In[72]:


#Variable "python" is used (var[0:2]) - This program prints the "python" substring starting at character 1 and ending at character 3, 
 #in that order (exclusive). As a result, the string "py" is printed.


var = "python"
print(var[0:2])


# In[73]:


#Variable "python" is used (var[0:5]) - This program prints the first six characters of the substring "python" starting from the first character (exclusive). 
 #As a result,the word "python" is printed in its entirety.


var = "python"
print(var[0:5])


# In[74]:


#This program also prints the entire string "python" as var = "python"nprint(var[0:6])". The reason is that because indexing is exclusive, 
 #var[0:6] includes every character in the string.


var = "python"
print(var[0:6])


# In[75]:


#Variable "python" is used (var[:5]) - This program replaces var[0:5] because the start index is not included. 
 #As a result, the string "pytho" is printed.


var = "python"
print(var[:5])


# In[76]:


#Variable "python" is used (var[:6]) - This program replaces var[0:6] because the start index is not included. 
 #As a result, the word "python" is printed in its entirety.


var = "python"
print(var[:6])


# In[77]:


#Variable "python" is used (var[0:]) - The substring of "python," starting at the first character and ending at the last character, 
 #is printed by this program. As a result, the word "python" is printed in its entirety.


var = "python"
print(var[0:])


# In[78]:


#Variable "python" is used (var[2:]) - The substring of "python," beginning with the third character and ending with the last character, 
 #is printed by this program. As a result, the string "thon" is printed.


var = "python"
print(var[2:])


# In[79]:


#Variable "python" is used (var[0:50]) - This program prints "pythonsubstring "'s beginning with character 1 and ending with character 50.
 #(exclusive). Since the string only contains six characters, the word "python" will be printed in its entirety.


var = "python"
print(var[0:50])


# In[80]:


#Variable "python" is used (var[5:25]) - This program prints the substring of "python," 
 #beginning at character six and ending at character twenty-five (exclusive). The string 'n' will be printed because it only contains six characters.



var = "python"
print(var[5:25])


# In[81]:


#This program uses the len() function to determine the length of the string "python" and prints the result, which is 6.


var = "python"
len(var)

