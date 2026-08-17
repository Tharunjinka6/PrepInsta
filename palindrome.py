#Method 1:Using simple Iteration
num_1=121
reverse_1=""
for i in str(num_1):
    reverse_1=i+reverse_1
if num_1==int(reverse_1):
    print("Palindrome")
else:
    print("Not a Palindrome")
#Method 2 using string slicing
num_2=131
reverse_2=int(str(num_2)[::-1])
if num_2==int(reverse_2):
    print("Palindrome")
else:
    print("Not a Palindrome")
#Method 3: Using Recurssion
def recurrev(number, rev):
    if number==0:
        return rev
    remainder=int(number%10)
    rev=(rev*10)+remainder
    return recurrev(int(number/10), rev)
number=121
rev=0
rev=recurrev(number, rev)
print(str(number)+ " is:", end="")
print("palindrome") if rev==number else print("Not palindrome")
#Method 4: using character matching
def checkPalindrome(str):
    for i in range(0, len(str)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
s="kayak"
print("Palindrome") if checkPalindrome(s) else print("Not a Palindrome")
#Method 5: Using Character Matching (updated)
def checkPalindrome(str):
    mid=int(len(str)/2)
    for i in range(0, mid):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
s_1="oxx"
print("Palindrome") if checkPalindrome(s_1) else print("Not a Palindrome")
#MEthod 6: Using in-built reversed function
def checkpalindrome_2(str_6):
    reverse_1=''.join(reversed(str_6))
    if str_6==reverse_1:
        return True
    return False
s_2="OXO"
print("Palindrome") if checkpalindrome_2(s) else print("not a palindrome")
#Method 7: Building reverse one chat at a time
string="123"
rev_1=""
for char in string:
    rev_1=char+rev_1
print("palindrome") if string == rev_1 else print("Not Palindrom")
print("string:" + str(string))
print("rev:" + str(rev_1))
#Method 8: using flag
string_1="radar"
j=-1
flag=0
for char in string_1:
    if char!=string_1[j]:
        flag=1
        break
    j=j-1
print("Not palindrome") if flag else print("palindrome")
#method 9 using backward slicing
str1="radar"
n=len(str1)
c=[]
for i in range(n - 1, -1, -1):
    c.append(str1[i])
rev="".join(c)
print(str1+"is: ",end="")
if str1==rev:
    print("Palindrome")
else:
    print("Not Palindrome")