#this script takes user input in base 10 and converts it to a desired base 
#prompt user input
num_inp=int(input("Please enter a number in base 10 \n"))

base_inp=int(input("Please select which base you would like to convert to. \nChoices: 2 8 10 16 \n"))

#base conversion
if base_inp == 10:
    base = 10 #define base for output
    num_int = num_inp #maintain input
elif base_inp == 2:
    base = 2 #define base for output
    num_int = bin(num_inp) #convert input
elif base_inp == 8:
    base = 8 #define base for output
    num_int = oct(num_inp) #convert input
elif base_inp == 16:
    base = 16 #define base for output
    num_int = hex(num_inp) #convert input
else:
    print("This base is not recognized. Please try again.") #reject base input
    exit()

#print output as string
product=str(num_int)
if base == 10:
    print("Your original value in base 10 is " + product + "\nWait... why did you run this script?")
else: 
    print("Your original value in base " + str(base) + " is " + product)