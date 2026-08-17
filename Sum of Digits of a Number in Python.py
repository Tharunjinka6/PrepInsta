#Method 1 Using String Character Extraction
num_1=input("Enter Number:")
sum_1=0
for i in num_1:
    sum_1=sum_1+int(i)
print(sum_1)
#method 2 Using Brute force
num_2=123
sum_2=0
while num_2!=0:
    digit=int(num_2%10)
    sum_2+=digit
    num_2=num_2//10
print(sum_2)
#Method 2 using recursion 1
num_3, sum_3=123, 0
def findSum(num_3, sum_3):
    if num_3==0:
        return sum_3
    digit_1=int(num_3%10)
    sum_3+=digit_1
    return findSum(num_3//10, sum_3)
print(findSum(num_3, sum_3))
#Method 4 using Recurssion 2
num_4=123
def findSum_1(num_4):
    if num_4==0:
        return 0
    return int(num_4%10)+findSum_1(num_4/10)
print(findSum_1(num_4))
#Method 4: Using ASCII Table
num_5, sum_5 = 123,0
for i in range(len(str(num_5))):
    sum_5+=ord(str(num_5)[i])-48
print(sum_5)
#Method 5 Using map(), sum() and strip methods
def getSum(n):
    num_str=str(n)
    list_of_num=list(map(int, num_str.strip()))
    print(list_of_num)
    return sum(list_of_num)
n=int(input("Enter the number:"))
print(getSum(n))
#Method 6:One Line recursive function
def sumDigits(n_1):
    return 0 if n_1==0 else int(n_1%10)+sumDigits(int(n_1/10))
n_1=int(input("Enter the number:"))
print(sumDigits(n_1))
#The cool method
n_2=[int(d) for d in input("Enter the number:")]
print("the sum of digits is:", sum(n_2))