def check(password):
    spl = ["!","@","#","$","_","-","*","&","/","\\"]
    length = len(pd) >= 8
    uppercase = any(i.isupper() for i in pd)
    lowercase = any(i.islower() for i in pd)
    digits = any(i.isdigit() for i in pd)
    special = any(i in spl for i in pd)

    if length & uppercase & lowercase & special & digits:
        print('''Strong password!
                \nUpdate your password periodically for better security!''')
    elif length & uppercase & lowercase:
        print('''Moderate password!
                \nAdd digits and/or special characters to create a stronger password!''')
    else:
        print('''Weak Password!
                \nUpdate a stronger password with the following:
                \n  (1) Eight or more characters in length
                \n  (2) Lowercase and Uppercase letters
                \n  (3) Mixture of special characters and digits''')

print("PASSWORD COMPLEXITY CHECKER")
pd = input("Enter your password: ")
check(pd)
