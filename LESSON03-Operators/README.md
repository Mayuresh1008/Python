# **Python Operators: A Comprehensive Guide**  
This repository provides an overview of **Python operators**, including arithmetic, comparison, logical, assignment, and ternary operators. Operators are essential for performing operations on variables and values in Python.  

---

## **📜 Types of Operators**  

### **1. Arithmetic Operators**  
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.  

| Operator | Description          | Example       |
|----------|----------------------|---------------|
| `+`      | Addition             | `5 + 3 = 8`   |
| `-`      | Subtraction          | `5 - 3 = 2`   |
| `*`      | Multiplication       | `5 * 3 = 15`  |
| `/`      | Division             | `5 / 2 = 2.5` |
| `%`      | Modulus (Remainder)  | `5 % 2 = 1`   |
| `**`     | Exponentiation       | `2 ** 3 = 8`  |
| `//`     | Floor Division       | `5 // 2 = 2`  |

---

### **2. Comparison Operators**  
Comparison operators are used to compare two values. They return `True` or `False`.  

| Operator | Description                  | Example         |
|----------|------------------------------|-----------------|
| `==`     | Equal to                     | `5 == 5 → True` |
| `!=`     | Not equal to                 | `5 != 3 → True` |
| `>`      | Greater than                 | `5 > 3 → True`  |
| `<`      | Less than                    | `5 < 3 → False` |
| `>=`     | Greater than or equal to     | `5 >= 5 → True` |
| `<=`     | Less than or equal to        | `5 <= 3 → False`|

---

### **3. Logical Operators**  
Logical operators are used to combine conditional statements.  

| Operator | Description                          | Example                          |
|----------|--------------------------------------|----------------------------------|
| `and`    | Returns `True` if both are true      | `(5 > 3) and (5 < 10) → True`    |
| `or`     | Returns `True` if at least one is true | `(5 > 3) or (5 < 2) → True`     |
| `not`    | Reverses the result                  | `not (5 > 3) → False`            |

---

### **4. Assignment Operators**  
Assignment operators are used to assign values to variables.  

| Operator | Description              | Example          |
|----------|--------------------------|------------------|
| `=`      | Assign                   | `x = 5`          |
| `+=`     | Add and assign           | `x += 3 → x = 8` |
| `-=`     | Subtract and assign      | `x -= 3 → x = 2` |
| `*=`     | Multiply and assign      | `x *= 3 → x = 15`|
| `/=`     | Divide and assign        | `x /= 2 → x = 2.5`|
| `%=`     | Modulus and assign       | `x %= 2 → x = 1` |
| `**=`    | Exponent and assign      | `x **= 2 → x = 25`|
| `//=`    | Floor divide and assign  | `x //= 2 → x = 2` |

---

### **5. Membership Operators**  
Membership operators are used to test if a value is present in a sequence (e.g., list, string).  

| Operator | Description                          | Example                  |
|----------|--------------------------------------|--------------------------|
| `in`     | Returns `True` if value is present   | `'a' in 'apple' → True`  |
| `not in` | Returns `True` if value is not present | `'b' not in 'apple' → True` |

---

### **6. Identity Operators**  
Identity operators are used to compare the memory locations of two objects.  

| Operator | Description                          | Example                  |
|----------|--------------------------------------|--------------------------|
| `is`     | Returns `True` if both are the same object | `x is y → True`       |
| `is not` | Returns `True` if both are not the same object | `x is not y → True` |

---

### **7. Ternary Operator**  
The ternary operator is a concise way to write conditional statements. It evaluates a condition and returns one of two values based on whether the condition is `True` or `False`.  

#### **Syntax**  
```python
value_if_true if condition else value_if_false
```  

#### **Example**  
```python
meaning = 15
print('Right on!') if meaning > 10 else print('Not Today')
```  

**Output**:  
```
Right on!
```  

In this example:  
- The condition `meaning > 10` is evaluated.  
- Since `meaning` is `15`, the condition is `True`, so `'Right on!'` is printed.  

---

## **🚀 How to Use This Repository**  
1. **Install Python**:  
   - Download and install Python from [python.org](https://www.python.org/).  

2. **Run the Code**:  
   - Copy the examples into a Python file (e.g., `operators.py`).  
   - Run the file using the command:  
     ```bash
     python operators.py
     ```  

3. **Experiment**:  
   - Modify the examples to test different operators and conditions.  

---

## **📚 What You’ll Learn**  
This repository covers the following Python concepts:  
1. **Arithmetic Operators**: Perform basic math operations.  
2. **Comparison Operators**: Compare values.  
3. **Logical Operators**: Combine conditions.  
4. **Assignment Operators**: Assign values to variables.  
5. **Membership Operators**: Check for values in sequences.  
6. **Identity Operators**: Compare object memory locations.  
7. **Ternary Operator**: Write concise conditional statements.  

---

