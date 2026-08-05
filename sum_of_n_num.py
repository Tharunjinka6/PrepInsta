#method-1
num=5
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)
#method-2
num_1=5
sum_1=int(num_1*(num_1+1)/2)
print(sum_1)
#method-3
def recursum(num_2):
  if num_2 == 0:
    return num_2
  return num_2 + recursum(num_2-1)
num_2, sum = 5,0
print(recursum(num_2))