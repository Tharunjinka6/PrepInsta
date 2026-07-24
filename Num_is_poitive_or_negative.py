#Brute_force
num=15
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")
#nested-if else
num=18
if num>0:
    if num==0:
        print("Zero")
    else:
        print("positive")
else:
    print("Negative")
#Ternary_operator
num=-10
print("positive" if num>0 else "Negative")