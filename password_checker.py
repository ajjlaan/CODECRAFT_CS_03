import re
def pass_check(password):
    remarks=[]
    strength=0
    if len(password) < 8:
        strength+=1
        remarks.append( "Too short")
    if not re.search("[A-Z]", password):
        strength+=1
        remarks.append( "No uppercase")
    if not re.search("[0-9]", password):
        strength+=1
        remarks.append("No digits")
    if not re.search("[!@#$%^&*]", password):
        strength+=1
        remarks.append("No special characters")
    if strength == 0:
        print( "Strong Password")
    else:
        print("WEAK")
        for r in remarks:
            
            print("-",r)


password = input("Input your password: ")

print("Password Strength -> ")
pass_check(password)


