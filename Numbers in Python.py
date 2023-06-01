#!/usr/bin/env python
# coding: utf-8

# In[3]:


#NUMBERS IN PYTHON


# In[4]:


#In Python, numbers are a fundamental data type used to represent numerical values in the code. There are three main types of numbers in Python: integers, floating-point numbers, and complex numbers.

#Integers: are positive or negative whole numbers with no decimal point. They can be defined by simply assigning a number to a variable, like so: x = 5. 
#Floating-point numbers, or floats: are numbers with a decimal point. They can be defined by adding a decimal point to the number, like so: y = 3.14.
#Complex numbers: on the other hand, have a real part and an imaginary part, and are defined by adding a suffix of 'j' or 'J' to the imaginary part, like so: z = 2 + 3j.

#Python provides a range of operations that can be performed on numbers, including arithmetic operations like addition, subtraction, multiplication, and division, as well as comparison operations like less than, greater than, equal to, and not equal to. These operations can be performed on both integer and floating-point numbers, but not on complex numbers.

#Python also provides a number of built-in functions that can be used to manipulate numbers, such as abs() to return the absolute value of a number, pow() to raise a number to a power, round() to round a floating-point number to a specified number of decimal places, and int() and float() to convert a number to an integer or floating-point number, respectively.

#Understanding how to work with numbers is an essential part of Python programming, as it is often used in calculations, data analysis, and other applications.


# In[5]:


#Integers: Integers are whole numbers, such as 1, 2, 3, and so on. They can be positive, negative, or zero. In Python, integers are represented using the int data type.


x = 4
y = -5
z = 0


# In[9]:


num = 85
type(num)


# In[10]:


num = 9845624
type(num)


# In[6]:


#Floating-point numbers: Floating-point numbers, or floats, are numbers that have a decimal point, such as 1.0, 2.5, or -3.14. In Python, floating-point numbers are represented using the float data type.


x = 4.5
y = -2.75
z = 0.0


# In[11]:


num = 5.43
type(num)


# In[7]:


#Complex numbers: Complex numbers are numbers that have a real part and an imaginary part, such as 3 + 2j or -4j. In Python, complex numbers are represented using the complex data type.


x = 2 + 3j
y = -1j
z = 4 - 2j


# In[13]:


num = 3+6j
type(num)


# In[14]:


num = 3+6j
num.real


# In[16]:


num = 3+6j
num.imag


# In[17]:


num = -8596.495
num


# In[18]:


num = -8596.495
print(num)


# In[20]:


#ARITHMETIC OPERATION'S 


# In[21]:


num1 = 75
num2 = 54
print(num1 + num2)


# In[22]:


num1 = 75
num2 = 54
print(num1 - num2)


# In[23]:


num1 = 75
num2 = 54
print(num1 * num2)


# In[24]:


num1 = 75
num2 = 54
print(num1 / num2)


# In[25]:


num1 = 75
num2 = 54
print(num1 // num2)


# In[26]:


num1 = 75
num2 = 54
print(num1 ** num2)


# In[27]:


num1 = 75
num2 = 54
print(num1 % num2)


# In[28]:


#CONVERSIONS


# In[29]:


#In Python, conversion refers to the process of changing the data type of a variable from one type to another. Python provides several built-in functions for conversion between data types.

#Some of the commonly used conversion functions include:

#int(): This function converts the given value to an integer data type. If the value is a floating-point number, the decimal part is truncated.

#float(): This function converts the given value to a floating-point number data type.

#str(): This function converts the given value to a string data type.

#bool(): This function converts the given value to a Boolean data type. It returns False for 0, None, empty strings, and empty lists or tuples. For all other values, it returns True.

#list(): This function converts the given value to a list data type.

#tuple(): This function converts the given value to a tuple data type.

#set(): This function converts the given value to a set data type.

#dict(): This function converts the given value to a dictionary data type.

#Conversions are often used in Python to handle user input, format data for output, or perform mathematical operations.


# In[31]:


# int() function example
num1 = int("4")
print(num1)


# In[32]:


# float() function example
num2 = float("5.0")
print(num2)


# In[33]:


# str() function example
num3 = 6
str_num3 = str(num3)
print(str_num3) 


# In[34]:


# bool() function example
bool_num1 = bool(num1)
print(bool_num1)


# In[35]:


# list() function example
list_nums = list((num1, num2, num3))
print(list_nums)


# In[36]:


# tuple() function example
tuple_nums = tuple((num1, num2, num3))
print(tuple_nums)


# In[37]:


# set() function example
set_nums = set((num1, num2, num3))
print(set_nums)


# In[38]:


# dict() function example
dict_nums = dict(num1=num1, num2=num2, num3=num3)
print(dict_nums)


# In[39]:


#In these examples, we convert a string to an integer using int(), a string to a float using float(), an integer to a string using str(), an integer to a boolean using bool(), and integers to a list, tuple, set, and dictionary using list(), tuple(), set(), and dict(), respectively.


# In[40]:


x = "254"
type(x)


# In[41]:


x = "254"
int(x)


# In[43]:


x = int(x)
type(x)


# In[44]:


x = "254"
x = float(x)
print(x)


# In[45]:


x = "254"
x = complex(x)
print(x)


# In[46]:


print (complex(3,8))


# In[47]:


#FUNCTIONS


# In[48]:


#In Python, a function is a block of organized and reusable code that performs a specific task. Functions help in breaking down large and complex programs into smaller and more manageable modules, which makes the code easy to read, understand, and maintain.

#Python functions are defined using the def keyword followed by the function name, parameters (if any), and a colon. The function body is then indented and contains the code that performs the desired task. Functions can return a value using the return statement, or they can modify the state of variables or objects outside of the function.

#Functions can be called by using the function name followed by parentheses and any arguments passed to the function. Python also provides built-in functions like print() and input().

#Functions can also have default parameter values, variable-length arguments, and can be defined as lambda functions (i.e., anonymous functions).

#Overall, functions are a fundamental concept in Python programming and are used extensively in writing efficient and organized code.


# In[49]:


x = -5.4
print(abs(x))


# In[50]:


import math
x = 20
print(math.exp(x))


# In[53]:


print(math.e)


# In[54]:


print(math.pi)


# In[55]:


x = 20
print(math.sqrt(x))


# In[57]:


print(math.sqrt(20))


# In[58]:


x = (245,3698,45879,14,1,254)
print(max)


# In[59]:


max(245,3698,45879,14,1,254)


# In[60]:


min(245,3698,45879,14,1,254)


# In[61]:


#LISTS


# In[62]:


#In Python, a list is a collection of items or elements that are ordered and changeable. Lists are one of the most commonly used data types in Python, and they can contain any type of data, including integers, floats, strings, and even other lists.

#Lists are defined using square brackets [ ] and elements within the list are separated by commas. Lists can be accessed and manipulated using indexing and slicing, where the index of the first element is 0.

#Lists have built-in functions and methods that can be used to perform various operations on the list, such as adding or removing elements, sorting, finding elements, and more. Some of the commonly used built-in functions with lists include len(), sorted(), min(), max(), and sum().

#Additionally, lists have several built-in methods that can be used to perform operations on the list. Some of these methods include append(), insert(), remove(), pop(), index(), sort(), and reverse(). These methods can be used to add or remove elements, sort the list, find the index of an element, and more.

#Overall, lists are a versatile and powerful data type in Python that can be used to store and manipulate large amounts of data in a variety of ways.


# In[63]:


# creating a list
my_list = [4, 2, 8, 5, 3]


# In[65]:


# adding an element to the end of the list
my_list = [4, 2, 8, 5, 3]
my_list.append(9)
print(my_list)


# In[66]:


# inserting an element at a specific index
my_list = [4, 2, 8, 5, 3]
my_list.insert(2, 7)
print(my_list)


# In[67]:


# removing an element from the list
my_list = [4, 2, 8, 5, 3]
my_list.remove(5)
print(my_list)


# In[68]:


# removing and returning the last element in the list
my_list = [4, 2, 8, 5, 3]
popped_element = my_list.pop()
print(my_list)


# In[69]:


# finding the index of an element
my_list = [4, 2, 8, 5, 3]
index_of_8 = my_list.index(8)
print(my_list)


# In[70]:


# sorting the list in ascending order
my_list = [4, 2, 8, 5, 3]
my_list.sort()
print(my_list)


# In[71]:


# reversing the order of the list
my_list = [4, 2, 8, 5, 3]
my_list.reverse()
print(my_list)


# In[72]:


# getting the length of the list
my_list = [4, 2, 8, 5, 3]
list_length = len(my_list)
print(my_list)


# In[73]:


# getting the smallest element in the list
my_list = [4, 2, 8, 5, 3]
smallest_element = min(my_list)
print(my_list)


# In[75]:


# getting the largest element in the list
my_list = [4, 2, 8, 5, 3]
largest_element = max(my_list)
print(my_list)


# In[76]:


# getting the sum of all elements in the list
my_list = [4, 2, 8, 5, 3]
sum_of_elements = sum(my_list)
print(my_list)


# In[77]:


#The append() method adds an element to the end of the list, the insert() method adds an element at a specific index, the remove() method removes a specified element from the list, and the pop() method removes and returns the last element in the list. The index() method returns the index of a specified element in the list.

#The sort() method sorts the list in ascending order, and the reverse() method reverses the order of the list.

#The len() function returns the length of the list, and the min(), max(), and sum() functions return the smallest element, largest element, and sum of all elements in the list, respectively.


# In[78]:


#Adding elements:


# In[79]:


# Using append()
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
print(fruits)


# In[98]:


# Using append()
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)


# In[80]:


# Using insert()
fruits = ['apple', 'banana', 'orange']
fruits.insert(1, 'grape')
print(fruits)


# In[99]:


# Using insert()
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)


# In[81]:


#Removing elements:


# In[82]:


# Using remove()
fruits = ['apple', 'banana', 'orange']
fruits.remove('banana')
print(fruits)


# In[100]:


# Using remove()
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)


# In[83]:


# Using pop()
fruits = ['apple', 'banana', 'orange']
last_fruit = fruits.pop()
print(last_fruit)
print(fruits)


# In[101]:


# Using pop()
my_list = [1, 2, 3]
last_element = my_list.pop()
print(last_element)
print(my_list)


# In[84]:


#Changing elements:


# In[85]:


fruits = ['apple', 'banana', 'orange']
fruits[1] = 'grape'
print(fruits)


# In[86]:


#Built-in functions:


# In[87]:


# Using len()
fruits = ['apple', 'banana', 'orange']
print(len(fruits))


# In[88]:


# Using sorted()
fruits = ['orange', 'banana', 'apple']
sorted_fruits = sorted(fruits)
print(sorted_fruits)


# In[93]:


# Using min()
numbers = [4, 2, 8, 1, 9]
print(min(numbers))


# In[92]:


# Using max()
numbers = [4, 2, 8, 1, 9]
print(max(numbers))


# In[91]:


# Using sum()
numbers = [4, 2, 8, 1, 9]
print(sum(numbers))


# In[94]:


#Built-in methods:


# In[95]:


# Using index()
fruits = ['apple', 'banana', 'orange']
index = fruits.index('banana')
print(index)


# In[96]:


# Using sort()
fruits = ['orange', 'banana', 'apple']
fruits.sort()
print(fruits)


# In[97]:


# Using reverse()
fruits = ['apple', 'banana', 'orange']
fruits.reverse()
print(fruits)


# In[102]:


#MORE CODES


# In[104]:


#CREATING LISTS


# In[103]:


num = [1,2,3,4,5,6,7]
print(num)


# In[105]:


letter = ['a','b','c','d','e','f']
print(letter)


# In[106]:


stg = ["dad","mom","son","daughter"]
print(stg)


# In[107]:


mix = [1,2,3,"dad","mom","son"]
print(mix)


# In[108]:


mat = [[1,2,3],['a','b','c']]
print(mat)


# In[109]:


#ACCESSING ELEMENTS IN LISTS


# In[110]:


mix = [1,2,3,"dad","mom","son"]
print(mix)


# In[111]:


mix = [1,2,3,"dad","mom","son"]
print (mix[3])


# In[112]:


mix = [1,2,3,"dad","mom","son"]
print (mix[-3])


# In[113]:


mix = [1,2,3,"dad","mom","son"]
print (mix[-2])


# In[114]:


mix = [1,2,3,"dad","mom","son"]
print (mix[:2])


# In[115]:


mix = [1,2,3,"dad","mom","son"]
print (mix[:3])


# In[116]:


mix = [1,2,3,"dad","mom","son"]
print (mix[2:])


# In[117]:


mix = [1,2,3,"dad","mom","son"]
print (mix[2:4])


# In[118]:


mix = [1,2,3,"dad","mom","son"]
print (mix[::2])


# In[119]:


mix = [1,2,3,"dad","mom","son"]
print (mix[::-2])


# In[120]:


#OPERATIONS ON LISTS


# In[121]:


x = ['hi']*100
print(x)


# In[138]:


x = [75]*100
print(x)


# In[125]:


letter = ['a','b','c','d','e','f']
print(letter)


stg = ["dad","mom","son","daughter"]
print(stg)


conc = letter + stg
print(conc)


# In[126]:


var = list("hey you")
print(var)


# In[127]:


var = list("heyyou")
print(var)


# In[128]:


var = list("hey you")
print(var)


var = list("heyyou")
print(var)


# In[129]:


num = [1,2,3,4,5,6,7]
print(num)


one,*other = num
print(one)
print(other)


# In[130]:


#METHODS IN LISTS


# In[131]:


num = [1,2,3,4,5,6,7]
print(num)


num.append(6)
print(num)


# In[132]:


num = [1,2,3,4,5,6,7]
print(num)


stg = ["dad","mom","son","daughter"]
print(stg)


num.extend(stg)
print(num)


# In[137]:


num = [1,2,3,4,5,6,7]
print(num)


num.insert(7,"grandma")
print(num)


# In[150]:


num.insert(7,"grandma")
print(num)


# In[151]:


num.remove("grandma")
print(num)


# In[153]:


var1 = ['b','f','a','q','r']
var1.sort()
print(var1)


# In[154]:


#BUILT-IN FUNCTIONS WITH LISTS


# In[155]:


y = [2,4,6,7,8,96,1]
print(y)


# In[156]:


y = [2,4,6,7,8,96,1]
len(y)


# In[157]:


y = [2,4,6,7,8,96,1]
min(y)


# In[158]:


y = [2,4,6,7,8,96,1]
max(y)


# In[159]:


y = [2,4,6,7,8,96,1]
sum(y)


# In[160]:


y = [2,4,6,7,8,96,1]
sum(y)/len(y)

