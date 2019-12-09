'''#Q1 max of three numbers:

def soft(x, y, z):
    if x > y and x > z:
        print("first is greater",x)
    elif y > z and y > x:
        print("second is greater",y)
    else:
        print("third is greater",z)


x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
z = int(input("Enter third number:"))

#Q2 fizz_buzz:
def fizz_buzz(s):
    if (s % 3 == 0) and (s % 5 ==0):
        return "fizzbuzz"

    elif s % 3 == 0:
        return "fizz"
    elif s % 5 == 0:
        return "buzz"
    else:
        return s



print("program started")
x = int(input("Enter any number:"))
ans =alisha(x)
if ans == True:
    print("x is even")
else:
    print("x is odd")


def largest (a,b,c):
    if a > b and a > c:
        return a
    elif b >a and b > c:
        return b
    else:
        return c

print("program started:")
a = int(input("Enter the first value:"))
b = int(input("Enter the second value:"))
c = int(input("Enter the third value:"))
large =largest(a,b,c)
print(f"The large among {a}, {b},{c} is {large}")



#Q3
def showNumbers(limit):
    for i in range(limit):
        if i % 2==0:
            print("even")
        else:
            print("odd")
num = int(input("Enter any number:"))
showNumbers(num)

#4

def fun (limit):
    sum=0
    for i in range(limit + 1):
        if i%3==0 or i%5==0:
            sum = sum+i
    print(sum)
a = int(input("Enter the limit:"))
fun(a)'''

#5

for i in range(1,4):
    for j in range(1,i + 1):
        print('*', end=" ")

print()

