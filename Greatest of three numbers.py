#Using if-else statement.
num1,num2,num3=20,10,30
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)
# Using Nested if-else Statements
num4,num5,num6=20,30,10
if num4>num5:
    if num4>num6:
        print(num4)
elif num5>num4:
    if num5>num6:
        print(num5)
else:
    print(num6)
#Using Ternary Operator
num7,num8,num9=20,30,10
max=num7 if num7>num8 else num8
max=num9 if num9>max else max
print(max)