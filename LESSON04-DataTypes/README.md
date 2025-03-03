# **Python Data Types**  
This repository provides an overview of **Python data types**, including strings, booleans, numeric types (integers, floats, complex numbers), and type casting. It also covers **string manipulation**, **escaping special characters**, and **checking variable types**.  

---

## **📜 Data Types in Python**  

### **1. Strings**  
Strings are sequences of characters enclosed in single (`' '`) or double (`" "`) quotes.  

#### **Literal Assignment**  
```python
first = "Dave"
last = "Gray"
```  

#### **Checking the Type of a Variable**  
Use `type()` to check the data type and `isinstance()` to verify if a variable is of a specific type.  
```python
print(type(first))  # <class 'str'>
print(type(first) == str)  # True
print(isinstance(first, str))  # True
```  

#### **Constructor Function**  
You can create strings using the `str()` constructor.  
```python
pizza = str("Pepperoni")
print(type(pizza))  # <class 'str'>
```  

#### **Concatenation**  
Combine strings using the `+` operator.  
```python
fullname = first + " " + last
print(fullname)  # Dave Gray
```  

#### **Casting a Number to a String**  
Convert numbers to strings using `str()`.  
```python
decade = str(1980)
print(type(decade))  # <class 'str'>
print(decade)  # 1980
```  

#### **Multiline Strings**  
Use triple quotes (`''' '''` or `""" """`) for multiline strings.  
```python
multiline = ''' 
Hey, how are you?

I was just checking in.   
                                All good?
'''
print(multiline)
```  

#### **Escaping Special Characters**  
Use backslashes (`\`) to escape special characters like quotes, tabs (`\t`), and newlines (`\n`).  
```python
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)
```  

#### **String Methods**  
Python provides built-in methods for string manipulation.  
```python
print(first.lower())  # dave
print(first.upper())  # DAVE
print(multiline.title())  # Capitalizes Each Word
print(multiline.replace("good", "ok"))  # Replaces "good" with "ok"
print(len(multiline))  # Returns the length of the string
```  

#### **String Formatting**  
Use methods like `center()`, `ljust()`, and `rjust()` for formatting.  
```python
title = "menu".upper()
print(title.center(20, "="))  # =======MENU========
print("Coffee".ljust(16, ".") + "$1".rjust(4))  # Coffee..........  $1
```  

#### **String Indexing and Slicing**  
Access individual characters or substrings using indexing.  
```python
print(first[1])  # a
print(first[-1])  # e
print(first[1:-1])  # av
print(first[1:])  # ave
```  

#### **Boolean Methods**  
Check if a string starts or ends with a specific substring.  
```python
print(first.startswith("D"))  # True
print(first.endswith("Z"))  # False
```  

---

### **2. Boolean Data Type**  
Booleans represent `True` or `False` values.  
```python
myvalue = True
x = bool(False)
print(type(myvalue))  # <class 'bool'>
print(isinstance(x, bool))  # True
```  

---

### **3. Numeric Data Types**  
Python supports integers, floats, and complex numbers.  

#### **Integers**  
Whole numbers without decimals.  
```python
price = 100
best_price = int(80)
print(type(price))  # <class 'int'>
```  

#### **Floats**  
Numbers with decimals.  
```python
gpa = 3.28
y = float(1.14)
print(type(gpa))  # <class 'float'>
```  

#### **Complex Numbers**  
Numbers with real and imaginary parts.  
```python
comp_value = 5 + 3j
print(type(comp_value))  # <class 'complex'>
print(comp_value.real)  # 5.0
print(comp_value.imag)  # 3.0
```  

---

### **4. Type Casting**  
Convert one data type to another using casting functions like `int()`, `float()`, `str()`, etc.  

#### **Casting a String to a Number**  
```python
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))  # <class 'int'>
```  

#### **Error Handling**  
Attempting to cast invalid data will raise an error.  
```python
# zip_value = int("New York")  # ValueError
```  

---

### **5. Built-in Functions**  
Python provides functions for mathematical operations.  

#### **Absolute Value**  
```python
print(abs(gpa))  # 3.28
```  

#### **Rounding**  
```python
print(round(gpa))  # 3
print(round(gpa, 1))  # 3.3
```  

#### **Math Module**  
Use the `math` module for advanced operations.  
```python
import math
print(math.pi)  # 3.141592653589793
print(math.sqrt(64))  # 8.0
print(math.ceil(gpa))  # 4
print(math.floor(gpa))  # 3
```  

---

## **🚀 How to Use This Repository**  
1. **Install Python**:  
   - Download and install Python from [python.org](https://www.python.org/).  

2. **Run the Code**:  
   - Copy the examples into a Python file (e.g., `datatypes.py`).  
   - Run the file using the command:  
     ```bash
     python datatypes.py
     ```  

3. **Experiment**:  
   - Modify the examples to test different data types and operations.  

---

## **📚 What You’ll Learn**  
This repository covers the following Python concepts:  
1. **Strings**: Creation, manipulation, and formatting.  
2. **Booleans**: True/False values and boolean methods.  
3. **Numeric Types**: Integers, floats, and complex numbers.  
4. **Type Casting**: Converting between data types.  
5. **Built-in Functions**: Mathematical operations and utilities.  

---
