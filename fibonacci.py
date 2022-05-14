from math import sqrt

#index = int(input("Enter a number: ")) - 1

def fibonacci(n):
    return ((1/sqrt(5))*((1+sqrt(5))/2)**n)-((1/sqrt(5))*((1-sqrt(5))/2)**n)

#print(fibonacci(index))
for i in range(-5, 5):
    print(round(fibonacci(i)))
