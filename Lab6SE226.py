import math

#Question 1
n = int(input("Enter value of n: "))
x = int(input("Enter value of x: "))

terms = [(lambda i: n**i/math.factorial(i))(i) for i in range(x+1)]

result = sum(terms)

result += 1

print(f"e^{n} = {result}")


#Question 2
sum = 0
user_input=int(input("Enter a number: "))
def calcSum(n):
    global sum
    if n == 0:
        return
    else:
        sum += (-1) ** (n + 1) / n
        calcSum(n - 1)

calcSum(user_input)
print("Sum:", sum)