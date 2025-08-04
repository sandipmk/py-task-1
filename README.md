# Elevate Lab Python Internship — Task 1 -> Build calculator CLI app.

## 📋 Task Overview
This repository contains **Task 1 -- calculator CLI app ** of the **Elevate Lab Python Internship Program** : 
Objective:
  - Create command-line calculator supporting basic operations.

key concept:
  - Functions.
  - Loops.
  - Conditionals.
  - CLI interaction.

---

##  📚 Approach

1. Understanding Requirements

  The task was to build a Command-Line Calculator using Python.
  The calculator needed to support Addition, Subtraction, Multiplication, and Division.


2. Function-Based Design

  Created separate functions for each arithmetic operation:
    addition(x, y)
    subtraction(x, y)
    multiplication(x, y)
    division(x, y) 


3. User Interaction Loop

  Used a while True loop to continuously prompt the user for an operation until they choose to exit.
  
  Displayed a menu of choices (+, -, *, /, Exit).
  
  Captured the user’s operation choice and validated it.
  

4. Input Validation

  Used try-except blocks to validate numeric inputs.

  If a user enters invalid data (like text), it shows an appropriate error message and prompts again.

  For division, added a check for division by zero to prevent runtime errors.

5. Performing Operations

  Based on user choice, the respective function is called with provided inputs.

  The result is displayed in a formatted output (e.g., 5 + 3 = 8).

6. Exit Condition

  If the user enters '0' as choice, the program prints an exit message and terminates.

7. Clean Code Practices

  Followed PEP8 coding style for naming and indentation.

  Structured the code with comments explaining key sections.

  Wrapped the execution in if __name__ == "__main__": block to ensure modular execution.

---

## 🛠️ Tools Used
- ** Python **
- ** VS code **
  
---

