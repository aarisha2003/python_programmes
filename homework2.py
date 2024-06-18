days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for weekdays in days:
    print(weekdays)

##########################################################################################################

#for table in range(2,21,2):
       
   #  int(input('2*',  )),print('=',table)

#############################################################################################################
# Define the correct unlock code
correct_code = "1234"

# Initialize variable for user input
user_input = ""

# Start a while loop to repeatedly ask for input until the correct code is entered
while user_input != correct_code:
    user_input = input("Enter the unlock code: ")
    if user_input == correct_code:
        print("Phone unlocked!")
    else:
        print("Incorrect code. Try again.")    
    
