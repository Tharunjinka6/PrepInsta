#using inner loop Range as[2, number-1]
#my code
num_1=10
for i in range(2,num_1-1):
    if i%1==0 and i%i==0 and i%2!=0:
        print(f"The num {i} is prime")

#prepInsta
low, high=2, 10
primes=[]
for i in range(low, high+1):
    flag=0
    if i<2:
        continue
    if i==2:
        primes.append(2)
        continue
    for x in range(2,i):
        if i%x==0:
            flag=1
            break
    if flag==0:
        primes.append(i)
print(primes)
#Method-2 using inner loop range as [2, number/2]
low_1, high_1=2, 10
primes_1=[2]
for num in range(low_1, high_1+1):
    flag_1=0
    if num<2:
        flag_1=1
    if num%2==0:
        continue
    iter=2
    while iter < int(num/2):
        if num%iter==0:
            flag_1=1
            break
        iter += 1
    if flag_1==0:
        primes_1.append(num)
print(primes_1)
#Method 3 using inner loop range as (2, sqrt(number))
low_2, high_2=2, 10
primes_2=[2, 3]
for num in range(low_2, high_2+1):
    flag_2=0
    if num<2:
        flag_2=1
    if num%2==0:
        continue
    if num%3==0:
        continue
    iter_1=2
    while iter_1 < int(pow(num, 0.5)):
        if num%iter_1==0:
            flag_2=1
            break
        iter_1 += 1
    if flag_2==0:
        primes_2.append(num)
print(primes_2)
#Method 4 Using inner loop range as [3,sqrt(number),2]
low_3, high_3=2, 10
primes_3=[2, 3]
for num in range(low_3, high_3+1):
    flag_3=0
    if num<2:
        flag_3=1
    if num%2==0:
        continue
    if num%3==0:
        continue
    iter_2=3
    while iter_2 < int(pow(num, 0.5)):
        if num%iter_2==0:
            flag_3=1
            break
        iter_2 += 1
    if flag_3==0:
        primes_3.append(num)
print(primes_3)


        


        
