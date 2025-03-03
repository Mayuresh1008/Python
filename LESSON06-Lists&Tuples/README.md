
# **Python Lists and Tuples**  
This repository provides an overview of **lists** and **tuples** in Python, including their creation, manipulation, and common methods. The code examples demonstrate how to work with these data structures effectively.  

---

## **📜 Lists in Python**  
Lists are **ordered, mutable collections** of items. They can store elements of different data types and are defined using square brackets `[]`.  

### **1. Creating Lists**  
```python
users = ['Dave', 'John', 'Sara']  # List of strings
data = ['Dave', 42, True]         # List with mixed data types
emptylist = []                    # Empty list
```  

### **2. Accessing List Elements**  
- Use **indexing** to access elements.  
- Negative indices count from the end of the list.  
```python
print(users[0])   # Dave
print(users[-2])  # John
```  

### **3. Slicing Lists**  
- Extract sublists using slicing.  
```python
print(users[0:2])  # ['Dave', 'John']
print(users[1:])   # ['John', 'Sara']
print(users[-3:-1]) # ['Dave', 'John']
```  

### **4. List Methods**  
#### **Adding Elements**  
- `append()`: Adds an element to the end.  
- `extend()`: Adds multiple elements from another iterable.  
- `insert()`: Inserts an element at a specific index.  
```python
users.append('Elsa')  # ['Dave', 'John', 'Sara', 'Elsa']
users.extend(['Robert', 'Jimmy'])  # ['Dave', 'John', 'Sara', 'Elsa', 'Robert', 'Jimmy']
users.insert(0, 'Bob')  # ['Bob', 'Dave', 'John', 'Sara', 'Elsa', 'Robert', 'Jimmy']
```  

#### **Modifying Elements**  
- Replace elements using slicing or indexing.  
```python
users[1:3] = ['Robert', 'JPJ']  # ['Bob', 'Robert', 'JPJ', 'Sara', 'Elsa', 'Robert', 'Jimmy']
```  

#### **Removing Elements**  
- `remove()`: Removes the first occurrence of a value.  
- `pop()`: Removes and returns the last element (or specified index).  
- `del`: Deletes an element or slice.  
- `clear()`: Empties the list.  
```python
users.remove('Bob')  # ['Robert', 'JPJ', 'Sara', 'Elsa', 'Robert', 'Jimmy']
print(users.pop())   # Jimmy (removes and returns the last element)
del users[0]         # ['JPJ', 'Sara', 'Elsa', 'Robert']
data.clear()         # [] (empties the list)
```  

#### **Sorting and Reversing**  
- `sort()`: Sorts the list in place.  
- `sorted()`: Returns a new sorted list.  
- `reverse()`: Reverses the list in place.  
```python
users.sort()  # Sorts in ascending order
nums = [4, 42, 78, 1, 5]
nums.reverse()  # Reverses the list
print(sorted(nums, reverse=True))  # Returns a new sorted list in descending order
```  

#### **Copying Lists**  
- Use `copy()`, `list()`, or slicing to create a copy.  
```python
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
```  

### **5. Checking Membership**  
- Use the `in` keyword to check if an element exists in the list.  
```python
print("Dave" in users)  # True or False
```  

---

## **📜 Tuples in Python**  
Tuples are **ordered, immutable collections** of items. They are defined using parentheses `()`.  

### **1. Creating Tuples**  
```python
mytuple = tuple(("Dave", 42, True))  # Tuple with mixed data types
anothertuple = (1, 4, 2, 8, 2, 2)   # Tuple of integers
```  

### **2. Accessing Tuple Elements**  
- Use indexing and slicing, similar to lists.  
```python
print(mytuple[0])  # Dave
print(anothertuple[1:3])  # (4, 2)
```  

### **3. Tuple Methods**  
- `count()`: Returns the number of occurrences of a value.  
- `index()`: Returns the index of the first occurrence of a value.  
```python
print(anothertuple.count(2))  # 3
print(anothertuple.index(2))  # 2
```  

### **4. Modifying Tuples**  
- Tuples are immutable, but you can convert them to lists, modify, and convert back.  
```python
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)  # ('Dave', 42, True, 'Neil')
```  

### **5. Unpacking Tuples**  
- Assign tuple elements to variables.  
```python
(one, *two, hey) = anothertuple
print(one)  # 1
print(two)  # [4, 2, 8, 2]
print(hey)  # 2
```  

---

## **🚀 What You’ll Learn**  
This repository covers the following Python concepts:  
1. **Lists**: Creation, indexing, slicing, and methods like `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, and `clear()`.  
2. **Tuples**: Creation, immutability, methods like `count()` and `index()`, and unpacking.  
3. **Copying Lists**: Using `copy()`, `list()`, and slicing.  
4. **Sorting and Reversing**: Using `sort()`, `sorted()`, and `reverse()`.  

---

