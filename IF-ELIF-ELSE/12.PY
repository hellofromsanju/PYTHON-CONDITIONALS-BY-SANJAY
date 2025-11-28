a=int(input(":"))
if a>=60:
    print("senior")
elif a>=20:
    print("adult")
elif a>=13:
    print("teenager")
elif 0<a and a<=12:
    print("Child")     
else:
    print("enter valid age")