#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TUPLES


# In[2]:


#In Python, a tuple is a collection of ordered and immutable elements enclosed within parentheses, separated by commas. Once a tuple is created, it cannot be modified or changed. This makes tuples useful for representing data that should not be modified, such as days of the week or coordinates on a map.

#Tuples are similar to lists in that they can store elements of any data type, such as integers, floats, strings, and even other tuples. However, tuples are immutable, so methods like append() or remove() cannot be used on them.

#To access elements in a tuple, indexing and slicing can be used, similar to lists. Tuples also have built-in functions and methods for working with them, such as len(), min(), and max().

#One common use case for tuples is in returning multiple values from a function. By returning a tuple of values, the function can easily return multiple pieces of information without needing to create multiple variables.


# In[5]:


# Create a tuple of coordinates
coordinates = (3.14, 5.58, 4.23, 2.71)
print(coordinates)


# In[7]:


# Accessing tuple elements with indexing
coordinates = (3.14, 5.58, 4.23, 2.71)
print(coordinates[2])


# In[8]:


# Accessing tuple elements with slicing
coordinates = (3.14, 5.58, 4.23, 2.71)
print(coordinates[1:2])


# In[9]:


# Using built-in functions and methods
print(len(coordinates))
coordinates = (3.14, 5.58, 4.23, 2.71)


# In[10]:


# Using built-in functions and methods
print(min(coordinates))
coordinates = (3.14, 5.58, 4.23, 2.71)


# In[11]:


# Using built-in functions and methods
print(max(coordinates))
coordinates = (3.14, 5.58, 4.23, 2.71)


# In[12]:


#Creating a tuple in Python is simple: just enclose a comma-separated sequence of elements in parentheses.


# In[13]:


my_tuple = (1, 2, 3)
print(my_tuple)


# In[14]:


#Tuples can contain elements of different data types, including numbers, strings, and even other tuples. Elements in a tuple can be accessed using indexing, just like in a list.

#Tuples have a number of built-in functions and methods that can be used to work with them. These include functions to get the length of a tuple (len()), find the minimum and maximum elements (min(), max()), and sum all elements (sum()). Tuples also have methods to find the index of a specified element (index()) and count the number of occurrences of a specified element (count()).

#While tuples are immutable, they can be reassigned to a new tuple with different values. This can be done using tuple unpacking, where each element in the tuple is assigned to a separate variable.


# In[18]:


#In this example, the variables a, b, and c are assigned the values 1, 2, and 3, respectively.


my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(my_tuple)


# In[16]:


my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)


# In[17]:


my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(my_tuple)


my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)


# In[19]:


#TYPES OF TUPLES


# In[25]:


#Immutable tuples: These are tuples whose values cannot be modified after creation.

# Creating an immutable tuple
my_tuple = (1, 2, 3)
print(my_tuple)


# In[24]:


# Creating an immutable tuple
my_tuple = (1, 2, 3)
my_tuple.append(2)
print(my_tuple)


# In[21]:


#Mutable tuples: These are tuples whose values can be modified after creation.


# Creating a mutable tuple
my_tuple = ([1, 2], 3, 4)
print(my_tuple)


# In[22]:


# Creating a mutable tuple
my_tuple = ([1, 2], 3, 4)
my_tuple[0].append(3)
print(my_tuple)


# In[26]:


#MORE CODES


# In[27]:


#CREATING TUPLES


# In[28]:


sales = ()
print(type(sales))


# In[29]:


sales = ()
print(sales)


# In[30]:


collages = ("SRM", "VIT", "NIT", "IIT")
print(collages)


# In[31]:


collages = ("SRM", "VIT", "NIT", "IIT")
print(type)


# In[32]:


collages = "SRM", "VIT", "NIT", "IIT",
print(collages)


# In[33]:


collages = ("SRM", "VIT", "NIT", "IIT")
print(collages)


collages = "SRM", "VIT", "NIT", "IIT",
print(collages)


# In[34]:


list1 = [1, 2, 3, 4, 5, 6]
print(list1)


# In[35]:


list1 = [1, 2, 3, 4, 5, 6]
print(type)


# In[36]:


list1 = [1, 2, 3, 4, 5, 6]
tuple1 = (1, 2, 3, 4, 5, 6)
print(list1)


# In[38]:


list1 = [1, 2, 3, 4, 5, 6]
tuple1 = (1, 2, 3, 4, 5, 6)
list1.append(5)
print(list1)


# In[39]:


list1 = [1, 2, 3, 4, 5, 6]
tuple1 = (1, 2, 3, 4, 5, 6)
tuple1.append(5)
print(list1)


# In[40]:


list1 = [1, 2, 3, 4, 5, 6]
tuple1 = (1, 2, 3, 4, 5, 6)
list1.append(5)
print(list1)


list1 = [1, 2, 3, 4, 5, 6]
tuple1 = (1, 2, 3, 4, 5, 6)
tuple1.append(5)
print(list1)


# In[41]:


#CONCATENATION


# In[42]:


#In Python, concatenation is the process of combining two or more tuples into a single tuple. Tuples can be concatenated using the + operator. When two or more tuples are concatenated, a new tuple is created that contains all the elements of the original tuples in the order they were concatenated.

#It's important to note that since tuples are immutable, concatenating two tuples does not modify the original tuples. Instead, a new tuple is created with the concatenated values.


# In[43]:


#Create two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1)
print(tuple2)


# In[46]:


#In this example, we first create two tuples named tuple1 and tuple2. We then use the + operator to concatenate them into a new tuple named concatenated_tuple. Finally, we print the concatenated tuple using the print() function.

#Concatenation can be useful in cases where you want to combine two or more tuples into a single tuple for processing.


#Concatenate the tuples using the + operator
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)


# In[49]:


#NESTING


# In[50]:


#In Python, tuples can contain elements of any data type, including other tuples. This is known as nesting, and it allows for the creation of more complex data structures.

#Nesting tuples is done by including a tuple as an element of another tuple. The nested tuple can be created independently and then added to the main tuple, or it can be created directly as an element of the main tuple.


# In[51]:


# Create a nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)


# In[54]:


# Accessing elements of the nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])


# In[55]:


# Accessing elements of the nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0][0])


# In[56]:


# Accessing elements of the nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1][1])


# In[57]:


#In this example, a nested tuple is created with three tuples as its elements. The elements of the nested tuple can be accessed using indexing and slicing, just like in a regular tuple.

#Nesting tuples can be useful for organizing data into a more structured format. For example, a list of coordinates could be stored as a nested tuple with each coordinate represented as a tuple of two numbers.


# In[59]:


collages = "SRM", "VIT", "NIT", "IIT",
print(collages)


num = (1,2,3,4,5,6,7)
print(num)


nest = (collages,num)
print(nest)


# In[60]:


collages = "SRM", "VIT", "NIT", "IIT",
print(collages)


num = [1,2,3,4,5,6,7]
print(num)


nest = (collages,num)
print(nest)


# In[61]:


#Repetition


# In[62]:


#In Python, repetition in tuples refers to creating a new tuple by repeating the elements of an existing tuple a certain number of times. This can be achieved by using the * operator followed by the number of times you want to repeat the tuple.


# In[65]:


rep = (1, 2, 3)
print(rep)


# In[66]:


rep = (1, 2, 3)
rep_t = my_tuple * 3
print(rep_t)


# In[67]:


#In this example, we first create a tuple called rep with three elements. We then use the * operator to repeat this tuple three times, and assign the result to a new tuple called rep_t. The output of the print statement is (1, 2, 3, 1, 2, 3, 1, 2, 3), which is the original tuple repeated three times.

#Note that the original tuple is not modified in this process, and a new tuple is created each time you use the * operator to repeat it. Also, if you try to multiply a tuple by a non-integer value, you will get a TypeError error.


# In[68]:


rep = ("github") * 45
print(rep)


# In[69]:


rep = ("github") * 45
print(rep)


rep = ("github ") * 45
print(rep)


rep = ("github",) * 45
print(rep)


# In[70]:


#Slicing


# In[71]:


#In Python, a tuple is an ordered collection of elements, enclosed in parentheses and separated by commas. Tuples are similar to lists, but they are immutable, meaning that their elements cannot be modified once they are created. Tuples support slicing, which allows you to extract a subset of elements from the tuple based on their position.


# In[ ]:


num = [1,2,3,4,5,6,7]
print(num)


# In[78]:


#Slicing in a tuple works in the same way as slicing in a list. You specify the starting and ending indices of the slice separated by a colon. For example, if you have a tuple num containing the elements (1, 2, 3, 4, 5, 6, 7), you can extract a slice containing the elements 2, 3

#This will output (2, 3, 4), which is the slice of the tuple starting at index 1 and ending at index 4 (exclusive). You can also use negative indices to slice the tuple from the end.



num = [1,2,3,4,5,6,7]
slice_t = num[1:4]
print(slice_t)


# In[77]:


#To extract a slice containing the last two elements of num

#This will output (6, 7), which is the slice of the tuple starting at the second-to-last element and ending at the end of the tuple.



num = [1,2,3,4,5,6,7]
slice_t = num[-2:]
print(slice_t)


# In[79]:


#Slicing can also be used to create a new tuple that contains a subset of the elements of an existing tuple. For example, to create a new tuple containing the elements (2, 3) from num

#This will output (2, 3), which is a new tuple containing the elements from my_tuple at indices 1 and 2.



num = [1,2,3,4,5,6,7]
slice_t = num[1:3]
print(slice_t)


# In[80]:


#UNPACKING


# In[1]:


#In Python, tuple unpacking is a way to assign the elements of a tuple to multiple variables in a single statement. This can be useful when working with functions that return multiple values, as well as for assigning values from a tuple to multiple variables.

#Tuple unpacking is done using a comma-separated list of variable names on the left-hand side of an assignment statement, and a tuple on the right-hand side. The number of variables on the left-hand side must match the number of elements in the tuple, or a "ValueError: too many values to unpack" or "ValueError: not enough values to unpack" will be raised.


# In[2]:


unp = (1,2,3,4,5)
print(unp)


# In[4]:


unp = (1,2,3,4,5)
a, b, c, d, e = unp
print(a)


# In[5]:


unp = (1,2,3,4,5)
a, b, c, d, e = unp
print(c)


# In[6]:


#In this example, we defined a tuple called unp with five elements. We then unpacked the tuple into three variables called a, b, c, d, and e using a single assignment statement. Finally, we printed the values of the variables.


# In[7]:


#Tuple unpacking can also be used to swap the values of two variables in a single statement, like this:


# Define two variables
a = 1
b = 2
print(a)
print(b)


# In[8]:


# Swap the values using tuple unpacking
a = 1
b = 2
a, b = b, a


# In[9]:


# Print the variables
a = 1
b = 2
a, b = b, a
print(a)
print(b)


# In[10]:


#In this example, we defined two variables a and b, and then swapped their values using tuple unpacking.


# In[11]:


#MORE CODE


# In[12]:


unp = ("github respiratray")
print(unp)


# In[13]:


unp = ("github respiratray")
tuple (unp)


# In[33]:


num = (1, 2, 3, 4)
print(num)


num = (1, 2, 3, 4)
a, b, c, d = num
print(a, b, c, d)


a, *b, c = num
print(a, b, c)


# In[34]:


#DELETING A TUPLE


# In[36]:


#In Python, tuples are immutable, which means that once they are created, their contents cannot be modified. Therefore, it is not possible to delete elements from a tuple. However, it is possible to delete the entire tuple using the del keyword.

#To delete a tuple, simply use the del keyword followed by the name of the tuple.

#In the above example, the entire my_tuple is deleted using the del keyword. After this, if we try to access the tuple, we will get an error because it no longer exists.

#Note that deleting a tuple is a permanent action and cannot be undone. Once a tuple is deleted, it cannot be recovered.


# In[41]:


num = (1, 2, 3, 4)
print(num)


# In[43]:


del num


# In[44]:


print(num)


# In[45]:


#BUILT IN FUNCTION


# In[46]:


#Tuples in Python come with a set of built-in functions and methods that can be used to work with them.

#In Python, there are several built-in functions that can be used to work with tuples:

#len(): returns the length of a tuple.
#max(): returns the maximum value in a tuple.
#min(): returns the minimum value in a tuple.
#sum(): returns the sum of all values in a tuple.
#any(): returns True if any element in a tuple is True, otherwise False.
#all(): returns True if all elements in a tuple are True, otherwise False.
#sorted(): returns a new sorted list of the elements in a tuple.
#enumerate(): returns an enumerate object that contains tuples of the index and value for each element in a tuple.
#zip(): returns a zip object that contains tuples of corresponding elements from two or more tuples.
#count(): returns the number of occurrences of a specified value in a tuple.
#index(): returns the index of the first occurrence of a specified value in a tuple.

#These built-in functions can be useful for performing various operations on tuples in Python.


# In[47]:


#len() function:
#The len() function returns the number of items in a tuple.


num = (1, 2, 3, 4, 5, 6)
print(len(num))


# In[48]:


#max() function:
#The max() function returns the maximum value from a tuple.


num = (1, 2, 3, 4, 5, 6)
print(max(num))


# In[49]:


#min() function:
#The min() function returns the minimum value from a tuple.


num = (1, 2, 3, 4, 5, 6)
print(min(num))


# In[50]:


#sum() function:
#The sum() function returns the sum of all elements in a tuple.


num = (1, 2, 3, 4, 5, 6)
print(sum(num))


# In[51]:


#any() function:
#The any() function returns True if any element in the tuple is true. Otherwise, it returns False


num = (0, 1, 2, 3, 4, 5, 6)
print(any(num))

num = (0, False, '', [], ())
print(any(num))


# In[52]:


#sorted() function:
#The sorted() function returns a new sorted list from the elements in the tuple.


num = (5, 2, 4, 6, 1, 3)
print(sorted(num))


# In[53]:


#enumerate() function:
#The enumerate() function takes an iterable and returns an iterator of tuples containing the index and value of each element.


num = (1, 2, 3, 4, 5, 6)
for index, value in enumerate(num):
    print(index, value)


# In[54]:


#zip() function:
#The zip() function takes two or more iterables and returns an iterator of tuples containing the corresponding elements from each iterable.


num1 = (1, 2, 3)
num2 = ('one', 'two', 'three')
result = zip(num1, num2)

for item in result:
    print(item)


# In[55]:


#count() function:
#The count() function returns the number of times a specified element appears in the tuple.


num = (1, 2, 3, 4, 5, 6)
print(num.count(2))


# In[56]:


#index() function:
#The index() function returns the index of the first occurrence of a specified element in the tuple.


num = (1, 2, 3, 4, 5, 6)
print(num.index(3))


# In[58]:


#CREATING A LIST TO TUPLE


# In[8]:


#In Python, it is possible to convert a list to a tuple using the tuple() function. The tuple() function takes a list as an argument and returns a tuple with the same elements as the list.



num = [1, 2, 3, 4, 5]
print(type(num))



num = [1, 2, 3, 4, 5]
print(num)



num = [1, 2, 3, 4, 5]
tup = tuple(num)
print(num)


print(type(tup))


# In[5]:


#In the above example, we created a list num with values 1 to 5, and then we converted it to a tuple using the tuple() function. The resulting tuple is (1, 2, 3, 4, 5).

#It is worth noting that when converting a list to a tuple, the resulting tuple is immutable, which means that its elements cannot be changed.


# In[7]:


#NESTING TUPLES IN A LIST


# In[9]:


#Nesting tuples in a list is a way to create a collection of data that contains multiple levels of information. In Python, a list can contain elements of any data type, including tuples. This means that a list can contain other lists or tuples, and those tuples can themselves contain other tuples or other data types.


# In[14]:


#To nest tuples in a list, you can simply create a list and include tuples as elements of the list. For example, consider the following code:


num = [(1, 2), (3, 4), (5, 6)]
print(num)



#In this example, my_list contains three tuples, each of which contains two elements. You can access the elements of the tuples in the list using indexing and slicing, just as you would with a regular tuple.


print(num[0])
print(num[1][0])
print(num[2][1])


#You can also nest lists and tuples to create more complex data structures. For example, consider the following code:


num = [(1, [2, 3]), (4, [5, 6])]


#In this example, my_list contains two tuples, each of which contains an integer and a list. You can access the elements of the nested lists using indexing and slicing, just as you would with regular lists



num = [(1, [2, 3]), (4, [5, 6])]
print(num[0][1][0])
print(num[1][1][1])


#Nesting tuples in a list can be useful for organizing data and creating complex data structures.


# In[16]:


#NESTING LISTS WITHIN A TUPLES


# In[26]:


#In Python tuples, you can also have lists as elements within them. This is known as nesting lists within tuples. The syntax for nesting lists within tuples is similar to nesting tuples within lists.


tup = (1, 2, [3, 4, 5], 6, [7, 8])
print(tup)


#In this example, we have a tuple with five elements. The third element and fifth element are lists. This is an example of nesting lists within tuples.

#You can access the elements of the nested list using indexing. For example, to access the first element of the third element of the tuple, you can use the following code:


tup = (1, 2, [3, 4, 5], 6, [7, 8])
tup[2][0]



#This would return the value 3.

#You can also modify the elements of the nested list. For example, to change the second element of the third element of the tuple, you can use the following code:


tup = (1, 2, [3, 4, 5], 6, [7, 8])
tup[2][1] = 10


#This would change the third element of the nested list from 4 to 10. However, you cannot modify the elements of the tuple itself since tuples are immutable.


# In[27]:


num = [1,2,3,4,5,6,7]
print(num)


# In[28]:


tup = (1, 2, [3, 4, 5], 6, [7, 8])
print(tup)


# In[29]:


tup = (1, 2, [3, 4, 5], 6, [7, 8])
tup[2][0]


# In[31]:


tup = (1, 2, [3, 4, 5], 6, [7, 8])
tup[2][1] = 10
print(tup)

