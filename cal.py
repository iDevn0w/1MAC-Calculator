try:
	print("--------------------------------------------------")
	print("Welcome to Arab Coder Calculator")
	print("Coded By Shwan Youssif with big loooooove 😍")
	print("license with @Arab_Coder_Community 😂")
	print("--------------------------------------------------")
	import random

	lst = random.choice(["x + y",  "12 + 23.4", "a ** b", "Hummanity is ONE divde by 0", "x / 0 = infinty(🙌)"])
	print("Hint !")
	print(lst)
	num1 = float(input("Enter the number: "))
	opr = input("Enter the oprator: ")
	num2 = float(input("enter the number2: "))

	def cal(x, z, y):
	   if opr == "+":
	      return print(f'Result = {x + y}')

	   elif opr == "-":
	      return print(f'Result = {x - y}')

	   elif opr == "/":
	      return print(f'Result = {x / y}')

	   elif opr == "**":
	      return print(f'Result = {x ** y}')

	   elif opr == "%":
	   	  return print(f'Result = {x % y}')

	   elif opr == "//":
	   	    return print(f'Result = {x // y}')

	   else:
	      print("Invild Value!")

	#try:
		#cal(num1, opr, num2)

	#except ZeroDivisionError:
		#print("you try to Change the World! 😉")


	cal(num1, opr, num2)

except ZeroDivisionError:
	print("you Try to Change the World! 😉")
