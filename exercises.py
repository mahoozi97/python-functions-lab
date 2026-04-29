def calculate_area_triangle(base, height):
    area = (base * height) / 2
    return area

print('Exercise 1:', calculate_area_triangle(10, 5))


def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

print("Exercise 2:", simple_interest(1000, 5, 2))


def apply_discount(price, rate):
    after_discount = price - rate / price * 100
    return after_discount

print("Exercise 3:", apply_discount(100, 25))


def convert_temperature(degree, type):
    if type == "C":
        return f"{(degree * 9/5) + 32} F"
    elif type == "F":
        return f"{(degree - 32) * 5/9} C"

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


def sum_to(n):
    return sum(range(1, n + 1))

print('Exercise 5:', sum_to(6))


def largest(*number):
    return max(number)

print('Exercise 6:', largest(8, 2, 3))


def calculate_tip(amount, percentage):
    return amount * (percentage / 100)

print('Exercise 7:', calculate_tip(50, 20))


def product(*numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

print("Exercise 8:", product(2, 5, 5))
print("Exercise 8:", product(1, -4))


def basic_calculator(num1, num2, operator):
    if operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2
    elif operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return num1 / num2

print("Exercise 9 Result:", basic_calculator(10, 5, "divide"))
