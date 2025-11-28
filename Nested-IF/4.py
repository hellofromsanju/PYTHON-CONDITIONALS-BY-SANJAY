p=input("enter your password: ")
if len(p)>=8:
    print("password is long enough")
    if "@" in p:
        print("password contains @")