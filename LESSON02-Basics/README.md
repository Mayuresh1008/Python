
# **Python Basics: Creating a Welcome Message**  
This repository demonstrates a simple Python program that prints a welcome message in a box format. It introduces basic Python concepts such as **variables**, **strings**, and **print statements**.  

---

## **📜 Code Overview**  
The program uses a combination of strings and print statements to create a visually appealing welcome message. Here's the code:  

```python
line01 = "********************"  # Header / Footer
line02 = "*                  *"  # Reusable line
line03 = "*     WELCOME!     *"  # Welcome message
line04 = "************"          # Unused in this example

# Start with a blank line
print('')
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)
```  

### **Output**  
When you run the program, it will display the following output:  

```
********************
*                  *
*     WELCOME!     *
*                  *
********************
```  

---

## **📝 Explanation of the Code**  

### **1. Variables and Strings**  
- **`line01 = "********************"`**:  
  - This creates a variable named `line01` and assigns it a string of asterisks (`*`).  
  - This line serves as the **header and footer** of the box.  

- **`line02 = "*                  *"`**:  
  - This creates a variable named `line02` and assigns it a string with asterisks on the sides and spaces in between.  
  - This line is reused to create the **top and bottom borders** of the box.  

- **`line03 = "*     WELCOME!     *"`**:  
  - This creates a variable named `line03` and assigns it a string with the welcome message centered between asterisks.  
 

### **2. Print Statements**  
- **`print('')`**:  
  - This prints a **blank line** to create space before the box.  

- **`print(line01)`**:  
  - Prints the header/footer line (`********************`).  

- **`print(line02)`**:  
  - Prints the reusable line (`*                  *`).  

- **`print(line03)`**:  
  - Prints the welcome message line (`*     WELCOME!     *`).  

- **`print(line02)`**:  
  - Reuses the reusable line to complete the box.  

- **`print(line01)`**:  
  - Prints the footer line to close the box.  

---

## **🚀 How to Run the Code**  
1. **Install Python**:  
   - If you don't have Python installed, download it from [python.org](https://www.python.org/).  

2. **Save the Code**:  
   - Copy the code into a file named `welcome.py`.  

3. **Run the Program**:  
   - Open a terminal or command prompt.  
   - Navigate to the folder where `welcome.py` is saved.  
   - Run the program using the command:  
     ```bash
     python welcome.py
     ```  

4. **Observe the Output**:  
   - The program will print the welcome message in a box format.  

---

## **📂 Repository Structure**  
This repository contains the following files:  
- `welcome.py`: The Python script that prints the welcome message.  
- `README.md`: This file, explaining the code and how to use it.  

---

## **📚 What You’ll Learn**  
This simple program introduces the following Python basics:  
1. **Variables**: Storing data for reuse.  
2. **Strings**: Working with text data.  
3. **Print Statements**: Displaying output to the console.  
4. **Code Reusability**: Using the same variable multiple times.  

---

