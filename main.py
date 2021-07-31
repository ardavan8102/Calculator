while True:
     print("Welcome My User !!")
     print("Math is not too Hard !!")
     # Add Numbers
     print("Enter 'add' to add two numbers")
     # Subtract Numbers
     print("Enter 'subtract' to subtract two numbers")
     # Multiply Numbers
     print("Enter 'multiply' to multiply two numbers")
     # Divide Numbers
     print("Enter 'divide' to divide two numbers")
     # Quiting Program
     print("Enter 'quit' to end the program")
     user_input = input("write: ")
     if user_input == "quit":
          print("exit")
          break
     elif user_input == "add":
          num1 = float(input("enter first number >> "))
          num2 = float(input("enter second number >> "))
          result = str(num1 + num2)
          print("the answer >>> "+ result)
     elif user_input == "subtract":
          num1 = float(input("enter first number >> "))
          num2 = float(input("enter second number >> "))
          result = str(num1 - num2)
          print("the answer >>> "+ result)
     elif user_input == "multiply":
          num1 = float(input("enter first number >> "))
          num2 = float(input("enter second number >> "))
          result = str(num1 * num2)
          print("the answer >>> "+ result)
     elif user_input == "divide":
          num1 = float(input("enter first number >> "))
          num2 = float(input("enter second number >> "))
          result = str(num1 / num2)
          print("the answer >>> "+ result)
     else: 
          print("unkhown input")
