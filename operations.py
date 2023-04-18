"""
Why int(numbers[0])?
First: numbers[0], this is because if we had initialized result as 0, the output
of the operation will change drastically. 
Example: numbers = (4, 2, 1), expected output = 1.
result = 0 - 4 = -4
result = -4 - 2 = -6
result = -6 - 1 = -7. Wrong output.

With result = int(numbers[0]) = result = 4.
(numbers is a tuple of strings, so type casting is necessary).
result = 4 - 2 = 2
result = 2 - 1 = 1. Correct output.

Second: numbers = numbers[1:], since the first value of the input is assigned to result,
we have to remove it to avoid duplication, and since numbers is a tuple,
slices are the way to go.
"""

def add(numbers: tuple[str]) -> int:
    result = int(numbers[0])
    numbers = numbers[1:]
    for number in numbers:
        result += int(number)
    return result 

def sub(numbers: tuple[str]) -> int:
    result = int(numbers[0])
    numbers = numbers[1:]
    for number in numbers:
        result -= int(number)
    return result

def mult(numbers: tuple[str]) -> int:
    result = int(numbers[0])
    numbers = numbers[1:]
    for number in numbers:
        result *= int(number)
    return result

def div(numbers: tuple[str]) -> int:
    result = int(numbers[0])
    numbers = numbers[1:]
    for number in numbers:
        result /= int(number)
    return result
