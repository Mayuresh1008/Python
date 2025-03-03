
# **Python Concepts: User Input, Random Module, Sys Module, Enum, and If-Else**  
This repository provides an overview of key Python concepts demonstrated through a simple **Rock-Paper-Scissors game**. The concepts covered include **user input**, **random module**, **sys module**, **import statements**, **enums**, and **if-else conditional statements**.  

---

## **📜 Concepts Covered**  

### **1. User Input in Python**  
Python uses the `input()` function to take user input. The input is always returned as a **string**, so you may need to convert it to other data types (e.g., `int`).  

#### **Example**  
```python
playerchoice = input("Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
player = int(playerchoice)
```  

- `input()` prompts the user to enter a value.  
- `int()` converts the string input to an integer.  

---

### **2. Random Module**  
The `random` module is used to generate random numbers or make random choices.  

#### **Example**  
```python
import random
computerchoice = random.choice("123")
computer = int(computerchoice)
```  

- `random.choice()` selects a random element from a sequence (e.g., `"123"`).  
- The result is converted to an integer for comparison.  

---

### **3. Sys Module**  
The `sys` module provides access to system-specific parameters and functions. One common use is to exit the program using `sys.exit()`.  

#### **Example**  
```python
import sys
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")
```  

- `sys.exit()` terminates the program and optionally displays a message.  

---

### **4. Import Statements**  
Python uses `import` to include external modules or libraries in your code.  

#### **Example**  
```python
import sys
import random
from enum import Enum
```  

- `import sys` and `import random` import the entire module.  
- `from enum import Enum` imports only the `Enum` class from the `enum` module.  

---

### **5. Enum in Python**  
Enums (enumerations) are used to define a set of named constants. They make code more readable and less error-prone.  

#### **Example**  
```python
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
```  

- `RPS.ROCK`, `RPS.PAPER`, and `RPS.SCISSORS` are named constants with integer values.  
- You can access enum values using `RPS(1)`, `RPS.ROCK`, or `RPS['ROCK']`.  

#### **Accessing Enum Values**  
```python
print(RPS(2))  # RPS.PAPER
print(RPS.ROCK)  # RPS.ROCK
print(RPS['ROCK'])  # RPS.ROCK
print(RPS.ROCK.value)  # 1
```  

---

### **6. If-Else Conditional Statements**  
Conditional statements are used to execute code based on certain conditions.  

#### **Example**  
```python
if player == 1 and computer == 3:
    print("🎉 You Win! 🎉")
elif player == 2 and computer == 1:
    print("🎉 You Win! 🎉")
elif player == 3 and computer == 2:
    print("🎉 You Win! 🎉")
elif player == computer:
    print("😳 Tie Game 😳")
else:
    print("🐍 Python Wins! 🐍")
```  

- `if` checks the first condition.  
- `elif` (else if) checks additional conditions if the previous ones are false.  
- `else` executes if none of the conditions are true.  

---

## **🚀 Rock-Paper-Scissors Game**  
The provided code implements a simple Rock-Paper-Scissors game using the concepts above.  

### **How It Works**  
1. The user is prompted to enter `1` for Rock, `2` for Paper, or `3` for Scissors.  
2. The computer randomly selects one of the three options.  
3. The program compares the user's choice with the computer's choice and declares the winner.  

### **Code Breakdown**  
```python
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playerchoice = input("Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")
    
computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.','') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".")
print("")

if player == 1 and computer == 3:
    print("🎉 You Win! 🎉")
elif player == 2 and computer == 1:
    print("🎉 You Win! 🎉")
elif player == 3 and computer == 2:
    print("🎉 You Win! 🎉")
elif player == computer:
    print("😳 Tie Game 😳")
else:
    print("🐍 Python Wins! 🐍")
```  

---

## **📚 What You’ll Learn**  
This repository covers the following Python concepts:  
1. **User Input**: Taking and processing user input.  
2. **Random Module**: Generating random choices.  
3. **Sys Module**: Exiting the program gracefully.  
4. **Import Statements**: Including external modules.  
5. **Enums**: Defining and using named constants.  
6. **If-Else Statements**: Making decisions in code.  

---
