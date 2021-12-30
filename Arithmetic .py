#Arithmetic operations:
def math():
	
	n1=int(input("Enter your first no.:"))
	n2=int(input("Enter your second no.:"))
	#Type of operation
	while True:
		choice=input("What would you like to do?")
		if choice in ("+","-","*","/"):
			
			if choice=="+":
				print("Addition: ",n1+n2)
				
			elif choice=="-":
				print("Substraction: ",n1-n2)
				
			elif choice=="*":
				print("Multiplication: ",n1*n2)
				
			elif choice=="/":
				if n2==0:
					print("Answer: ","Infinity")
				else:
					print("Division: ",n1/n2)
					
			while True:
				repeat=input("Would you like to do it again?")
				if repeat in ("YES","Y","yes","y"):
					math()
				elif repeat in ("NO","N","no","n"):
					print("!!!Thank you!!!")
					exit()
				else:
					print("Invalid input")
		else:
					print("Invalid input")
					
math()