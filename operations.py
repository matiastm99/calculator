def add(numbers):
    result = int(numbers[0])
    numbers = numbers[1:]
    for number in numbers:
        result += int(number)
    return result 

def sub(numbers):
    result = int(numbers[0])
    numbers = numbers[1:]
    for number in numbers:
        result -= int(number)
    return result

def mult(numbers):
    result = int(numbers[0])
    numbers = numbers[1:]
    for number in numbers:
        result *= int(number)
    return result

def div(numbers):
    result = int(numbers[0])
    numbers = numbers[1:]
    for number in numbers:
        result /= int(number)
    return result
    