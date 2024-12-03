name = str(input("Enter your name: "))
count = 0
test = 0
print("Menu: \n***** \nU Uppercase \nL Lowercase \nA Alternate")

options = str(input("(U-L-A): "))
while options.upper() not in ["U", "L", "A"]:
    options = str(input("(U-L-A): "))

if options.upper() == "U":
    print(name.upper())
elif options.upper() =="L":
    print(name.lower())
elif options.upper() == "A":
    while count < len(name):
        if test == 0:
            print(name[count].upper(), end='')
        else:
            print(name[count].lower(), end= '')
        count +=1
        test = count % 2
        
    
