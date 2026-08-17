#Method 1 using simple iteration
num_1=123
temp=num_1
reverse=0
while num_1>0:
    remainder=num_1%10
    reverse=(reverse*10)+remainder
    num_1=num_1//10
print(reverse)
#Method 2
num_2=123
print(str(num_2)[::-1])
#Method 3
def recursum(number, reverse_1):
    if number == 0:
        return reverse_1
    remainder = int(number % 10)
    reverse_1 = (reverse_1 * 10) + remainder
    return recursum(int(number / 10), reverse_1)
number = 123
reverse_1 = 0
print(recursum(number, reverse_1))