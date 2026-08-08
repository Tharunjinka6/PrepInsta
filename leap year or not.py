#Using if-else Statements 1
year=2024
if (year%400==0) or (year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("Not a leap year")

#Using if-else Statements 2
year_1=2024
if(((year_1%4==0) and (year_1%100!=0)) or (year_1%400==0)):
    print("Leap Year")
else:
    print("Not a Leap Year")

#Using Ternary Operator
def is_leap_year(year_2):
    return True if (year_2%4==0 and year_2%100!=0) or (year_2%400==0) else False
year_2=2024
print(f"{year_2} is a leap year: {is_leap_year(year_2)}")

#Using Calendar Module
import calendar
def is_leap_year_3(year_3):
    return calendar.isleap(year_3)
year_3=2024
print(f"{year_3} is a leap year: {is_leap_year_3(year_3)}")

#Using Lamda Function
is_leap_year_4 = lambda year_4: True if (year_4 % 4 == 0 and year_4 % 100 != 0) or (year_4 % 400 == 0) else False
year_4=2024
print(f"{year_4} is a leap year: {is_leap_year_4(year_4)}")