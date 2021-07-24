i=0
while i <= 0:
  print("bismillshi Ar rahmon ar raheem")
  print("this is a simple calculator")
  print("enter your operands_1:")
  operand_1 = input()
  print("enter operand_2:")
  operand_2 = input()
  print("enter '+' to add up numbers")
  print("ENTER '-' TO SUBTRACT NUMBERS")
  print("enter '/' to divide numbers")
  print("enter '*' to multiply numbers")
  print("enter '!' to terminate the program")
  def ADD():
    result = int(operand_1) + int(operand_2)
    print(result)

  def SUBTRACT():
    result = int(operand_1) - int(operand_2)
    print(result)

  def DIVIDE():
    result = int(operand_1) / int(operand_2)
    print(result)

  def MULTIPLY():
    result = int(operand_1) * int(operand_2)
    print(result)  

  sign_input = input()
  if sign_input == "!":
    print("operation terminated!!")
    break
  
  if sign_input == "+":
    print(operand_1,sign_input,operand_2)
    ADD()
  elif sign_input =="-":
    print(operand_1,sign_input,operand_2)
    SUBTRACT()  
  elif sign_input =="/":
    print(operand_1,sign_input,operand_2)
    DIVIDE()
  elif sign_input =="*":
    print(operand_1,sign_input,operand_2)
    MULTIPLY()
  

