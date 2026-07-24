#Brute_force
num=10
if num%2==0:
    print("Even")
else:
    print("odd")
#Ternery operator
num=15
print("even" if num%2==0 else "Odd")
#BitWise Operator
def isEven(num):
  return not num&1
if __name__ == "__main__":
  num = 13
  if isEven(num):
    print('Even')
  else:
    print('Odd')