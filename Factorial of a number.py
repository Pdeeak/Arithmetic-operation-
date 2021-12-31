#Factorial of a number:-
def factorial():
	#Ask user to enter a number
	number=int(input("Enter your number: "))
	
	result=1
	
	if number<0:
		print("Factorial does not exist for negative number.")
		
	elif number==0:
		print("Factorial of 0 is 1.")
		
	else:
		for i in range(1,number+1):
			result=result*i
		print("The factorial of your number is :",result)
		while True:
			#Asking user to repeat the function
			repeat=input("\nWould you like to do it again?")
			if repeat in("YES","Y","yes","y"):
				factorial()
				
			elif repeat in("NO","N","no","n"):
				print("!!!Thank you!!!")
				exit()
				
			else:
				print("Sorry invalid input")
				
factorial()