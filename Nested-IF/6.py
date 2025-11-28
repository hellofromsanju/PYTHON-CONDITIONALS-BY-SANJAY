h=input("enter your string: ").lower()

if h.isalpha():
    print("its alphabet")
    if h in "aeiou":
        print("its a vowel")