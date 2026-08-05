#Method-1
num1,num2=5,10
sum=0
for i in range(num1,num2+1):
    sum=sum+i
print(sum)
#Method-2
num3,num4=5,10
sum_1=int((num4*(num4+1)/2)-(num3*(num3+1)/2)+num3)
print(sum_1)
#Method-3
def recursum(sum_2,num5,num6):
  if num5>num6:
    return sum_2
  return num5+recursum(sum_2,num5+1,num6)
num5,num6=5,10
sum_2=0
print(recursum(sum_2,num5,num6))
