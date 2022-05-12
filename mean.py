from math import sqrt

def arithmetic_mean(array):
    return sum(array) / len(array)

def geometric_mean(array):
    factor = 1
    for number in array:
        factor *= number
    return factor ** (1/len(array))

while True:
    numbers = [eval(number) for number in input(">").split()]
    if numbers[0] == 0:
        break
    print(f"Arithmetic mean: {arithmetic_mean(numbers)}")
    print(f"Geometric mean: {geometric_mean(numbers)}")
