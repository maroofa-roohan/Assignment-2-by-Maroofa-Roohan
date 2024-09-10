# -*- coding: utf-8 -*-
"""Assignment 2 by Maroofa Roohan

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QFURQ2_wnMXMdkBlRA1S62HohIlody1E
"""

#assignment 2

#string slicing with example
#String slicing in Python allows you to extract a substring from a string by specifying a range of indices.
#The syntax for string slicing is:
#string[start:end:step]

text = "Python Programming"

# Slice from index 7 to 11 (excluding 11)
slice1 = text[7:11]   # Output: "Prog"

# Slice the first 6 characters
slice2 = text[:6]     # Output: "Python"

# Slice the last 6 characters
slice3 = text[-6:]    # Output: "mming"

# Slice every third character from the whole string
slice4 = text[::3]    # Output: "Ph rgn"

print(slice1, slice2, slice3, slice4)

#The key features of lists in Python:
#Ordered
#Mutable
#Heterogeneous
#Dynamic Size
#Indexing and Slicing
#Nested Lists
#Built-in Functions and Methods

#To access elements in a list, we use their index inside square brackets. For example, the first element is accessed with index 0.
#To modify elements in a list, we assign a new value to a specific index. This replaces the original value at that position.
#To delete elements
#del to remove an element by its index.
#remove() to delete an element by its value (the first occurrence).
#pop() to remove an element by its index and return the removed element.
#These methods allow you to manage elements in a list efficiently.
my_list = [10, 20, 30, 40]
print(my_list[1])  # Output: 20 (access element at index 1)

my_list[2] = 99  # Modifying the element at index 2
print(my_list)  # Output: [10, 20, 99, 40]

del my_list[1]  # Deletes element at index 1
print(my_list)  # Output: [10, 99, 40]

my_list.remove(99)  # Removes the element with value 99
print(my_list)  # Output: [10, 40]

popped_element = my_list.pop(0)  # Removes and returns the element at index 0
print(popped_element)  # Output: 10
print(my_list)  # Output: [40]

#List                                                           	Tuple
#	Mutable (can modify after creation)                      	Immutable (cannot modify after creation)
#	Defined using square brackets [ ]                          	Defined using parentheses ( )
# Modification	Can change size (add or remove elements)	      Fixed size once created
#	Slower due to mutability                                    	Faster due to immutability
#	When data needs to change	                                     When data should remain constant
#Supports methods like append(), remove(), etc.                	Limited methods, no append() or remove()
#Example:
# List example
my_list = [1, 2, 3]
my_list[0] = 10      # Modifying an element
my_list.append(4)    # Adding an element
print(my_list)       # Output: [10, 2, 3, 4]

# Tuple example
my_tuple = (1, 2, 3)
# my_tuple[0] = 10   # Error: cannot modify a tuple
print(my_tuple)      # Output: (1, 2, 3)
#Lists are used when you need to change or modify data.
#Tuples are ideal when the data should remain unchanged.

# The key features of sets inn python
#Unordered
#Unique Elements
#Mutable
#No Indexing or Slicing
#Set Operations
#Efficient Membership Testing
# Creating a set
my_set = {1, 2, 3, 4, 4}  # Duplicates are removed automatically
print(my_set)  # Output: {1, 2, 3, 4}

# Adding an element
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Removing an element
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))        # Union: {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # Intersection: {3}

# Use Cases of Tuples:
#1. Immutable Data: # We use tuples when we need a fixed collection of items that should not be changed, such as coordinates or fixed configuration values.
#2. Dictionary Keys: # We can use tuples as keys in dictionaries, while lists cannot be used for this purpose.
#3. Function Return Values: # We return multiple values from functions as tuples, which allows for easy unpacking of results.
#4. Data Integrity: # We use tuples to ensure data remains constant throughout the program, helping maintain data integrity.

### Use Cases of Sets:
#1. Unique Collections: # We use sets when we need a collection of unique items and want to automatically eliminate duplicates.
#2. Set Operations: # We utilize sets for mathematical operations like union, intersection, and difference.
#3. Membership Testing: # We use sets for fast membership testing to check if an item is present in the collection.
#4. Removing Duplicates: # We use sets to remove duplicate elements from lists or other iterables.

#Each data structure serves its own purpose, and choosing between them depends on our specific requirements.

# add,modify, delete, items in dictionary
my_dict = {'name': 'Alice', 'age': 25}

# Adding a new key-value pair
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Modifying an existing key-value pair
my_dict['age'] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Deleting an item using `del`
del my_dict['city']
print(my_dict)  # Output: {'name': 'Alice', 'age': 26}

# Deleting an item using `pop()`
removed_value = my_dict.pop('age')
print(removed_value)  # Output: 26
print(my_dict)  # Output: {'name': 'Alice'}

# immutability of dictionary keys is essential for maintaining consistent hash values, ensuring data integrity, and supporting efficient operations

# Examples illustrating the importance of immutable dictionary keys:

### 1. **Hashing Requirement**
# Immutable types like strings work as dictionary keys, but mutable types like lists do not.


# Correct usage with immutable key (string)
my_dict = {"name": "Alice"}
print(my_dict["name"])  # Output: Alice

# Incorrect usage with mutable key (list)
# my_dict = {[1, 2, 3]: "Invalid"}  # Raises TypeError: unhashable type: 'list'


### 2. **Data Integrity**
 #Immutable keys prevent accidental modification that could disrupt the dictionary structure.


#my_dict = {(1, 2): "Point"}  # Tuple is immutable
# my_dict[[1, 2]] = "Invalid"  # Lists are mutable, will raise a TypeError


### 3. **Efficient Lookups**
#- Immutability ensures consistent hash values for fast access.


my_dict = {1: "One", 2: "Two"}
print(my_dict[1])  # Efficient lookup, Output: One


### 4. **Avoids Errors**
#- Using mutable keys can lead to unpredictable behavior.


# Imagine we could use a list as a key (which is not allowed)
# Modifying the list would cause issues with retrieving data
my_dict = {(1, 2): "Valid tuple"}
# If the key could be changed, finding the original entry would become impossible.

#These examples highlight the importance of keeping dictionary keys immutable.
