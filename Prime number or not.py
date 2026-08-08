#Simple iterative solution
num_1=15
flag=0
for i in range(2,num_1):
    if num_1%i==0:
        flag=1
        break
if flag==1:
    print("Not a prime")
else:
    print("Prime")
#Optimization by break condition
num_2=15
flag_1=0
if num_2<2:
    flag_1=1
else:
    for i in range(2,num_2):
        if num_2%i==0:
            flag_1=1
            break
if flag_1==1:
    print("Not a prime")
else:
    print("Prime")

# Optimization by n/2 iterations
num_3=15
flag_2=0
if num_3<2:
    flag_2=1
else:
    for i in range(2,int(num_3/2)+1):
        if num_3%i==0:
            flag_2=1
            break
if flag_2==1:
    print("Not a prime")
else:
    print("Prime")

#Optimization by √n
num_4=15
flag_3=0
if num_4<2:
    flag_3=1
else:
    for i in range(2,int(pow(num_4,0.5)+1)):
        if num_4%i==0:
            flag_3=1
            break
if flag_3==1:
    print("Not a prime")
else:
    print("Prime")
#Optimization by skipping even iteration
num_5=15
flag_4=0
if num_5<2:
    flag_4=1
elif num_5==2:
    flag_4=0
else:
    for i in range(3,int(pow(num_5,0.5)+1),2):
        if num_5%i==0:
            flag_4=1
            break
if flag_4==1:
    print("Not a prime")
else:
    print("Prime")

#Basic Recursion technique
num_6 = 15
def checkPrime(num_6,iter=2):
  if num_6 == iter:
    return True
  if num_6%iter==0:
    return False
  if num_6<2:
    return False
  return checkPrime(num_6,iter+1)
if checkPrime(num_6)==True:
  print("Prime")
else:
  print("Not a Prime")