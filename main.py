print("Question 1")
print("// מחלק את המספר למספר שלם")
print("% מודולו מראה את שארית החילוק")
print("Question 2")
book = int(input("enter the number of the books"))
print(book)
print("number of shelves ", book // 15,"number of books in the cart" ,book % 15)
print("Question 3")
capsule = int(input("enter the number of students"))
print(capsule)
if capsule % 20 >= 1:
  print(capsule // 20 + 1)
else:
  print(capsule // 20)
print("Question 4 A")
num = int(input("Enter any number between 9 to 99"))
print(num)
if num < 10:
 print("erorr")
elif num > 100:
  print("erorr")
else:
  print(num % 10 + num // 10)
print("Question 4 B")
number = int(input("enter any number between 100 to 999"))
print(number)
if number < 100:
  print("erorr")
elif number > 999:
  print("erorr")
else:
  print(number % 10 + number % 100 // 10 + number // 100)
num2 = int(input("Enter any number between 9 to 99"))
print(num2)
if num2 < 10:
 print("erorr")
elif num2 > 100:
  print("erorr")
ahadot = (num2 % 10)
asarot = (num2 // 10)
print(ahadot * 10+asarot + 1)
number2 = int(input("enter any number between 100 to 999"))
print(number2)
if number2 < 100:
  print("erorr")
elif number2 > 999:
  print("erorr")
else:
 ahadot2 = (number2 % 10)
 asarot2 = (number2 % 100 // 10)
 meot = (number2 // 100)
 print(ahadot2 * 100 + asarot2 * 10 + meot + 1)
boom = int(input("enter a number"))
if boom % 7 == 0:
 print("boom")
elif str(boom).find("7"):
  print("boom")
else:
  print("Try again")