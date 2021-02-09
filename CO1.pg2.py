a=2021
b = int(input("Enter end year: "))

if(a<b):
    print("Leap year are:")
    for i in range(a, b):
        if (i % 4 == 0 and i % 100 != 0 or i % 4 == 0 and i % 400 == 0):
            print(i)
else:
    print("Invalid Year")



