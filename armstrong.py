#Method using iteration
number=371
num=number
total=0
length=len(str(num))
def checkArmstrong(num,length,total):
    if num==0:
        return total
    total+=pow(int(num%10),length)
    return checkArmstrong(num//10,length,total)
if checkArmstrong(num,length,total)==number:
    print("Armstrong")
else:
    print("Not Armstrong")
#Using Recursion
number_1=371
num_1=number_1
digit_1,total_1=0,0
length_1=len(str(num_1))
for i in range(length_1):
    digit_1=int(num_1%10)
    num_1=num_1//10
    total_1+=pow(digit_1,length_1)
if total_1==number_1:
    print("Armstrong")
else:
    print("Not Armstrong")