from getpass import getpass

print('A good password should be at least 8 characters long, include an number, and include a special character. To see if your password meets those requirements and is "Secure", enter it below.')

password = getpass('Password: ')
spec = "!@#$%^&*()_+=-[]{}`/?~;:'/\""

passlength = len(password)

def check(input):
    number = False
    special = False
    length = False

    for letter in input:

        if letter.isdigit():
            number = True

        if letter in spec:
            special = True

        if passlength > 8:
            length = True

        if special and number and length == True:
            return True
        
    if number == True and special == False and length == False:
        print("You might want to add a special character and make it longer.")
    elif number == True and special == False and length == True:
        print("You might want to add a special character.")

    elif number == True and special == True and length == False:
        print("You might want to make the password longer")
    elif number == False and special == True and length == True:
        print("You might want to add a number. ")

    elif number == False and special == False and length == True:
        print("You might want to add a number and a special character.")
    elif number == False and special == True and length == True:
        print("You might want to add a number. ")
 
if check(password) == True:
    print("Your password is secure")
else:
    print("Your password is not secure")

# print(password)
