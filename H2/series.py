# Importing libraries
from math import pow, log10

# 1. Palindrome Series
# Checks if a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Generates a list of palindrome numbers up to a limit
def generate_palindrome_series(limit):
    return [num for num in range(limit) if is_palindrome(num)]

# Example usage:
print("Palindrome Series:", generate_palindrome_series(1000))


# 2. Armstrong Numbers Series
# Checks if a number is an Armstrong number
def is_armstrong(num):
    num_digits = int(log10(num) + 1) if num > 0 else 1  # Calculate the number of digits
    return num == sum(int(digit) ** num_digits for digit in str(num))

# Generates a list of Armstrong numbers up to a limit
def generate_armstrong_series(limit):
    return [num for num in range(limit) if is_armstrong(num)]

# Example usage:
print("Armstrong Series:", generate_armstrong_series(1000))


# 3. Lucas Numbers Series
# Generates Lucas numbers up to a given count
def generate_lucas_series(count):
    lucas_series = [2, 1]
    while len(lucas_series) < count:
        lucas_series.append(lucas_series[-1] + lucas_series[-2])
    return lucas_series[:count]

# Example usage:
print("Lucas Series:", generate_lucas_series(10))


# 4. Fibonacci Series (for comparison)
# Generates Fibonacci numbers up to a given count
def generate_fibonacci_series(count):
    fibonacci_series = [0, 1]
    while len(fibonacci_series) < count:
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series[:count]

# Example usage:
print("Fibonacci Series:", generate_fibonacci_series(10))


# 5. Perfect Numbers Series
# Checks if a number is a perfect number
def is_perfect(num):
    return num == sum(div for div in range(1, num // 2 + 1) if num % div == 0)

# Generates a list of perfect numbers up to a limit
def generate_perfect_series(limit):
    return [num for num in range(2, limit) if is_perfect(num)]

# Example usage:
print("Perfect Series:", generate_perfect_series(1000))

from math import factorial, sqrt

# 6. Catalan Numbers Series
# Generates Catalan numbers up to a given count
def generate_catalan_series(count):
    return [factorial(2 * n) // (factorial(n + 1) * factorial(n)) for n in range(count)]

# Example usage:
print("Catalan Series:", generate_catalan_series(10))


# 7. Triangular Numbers Series
# Generates triangular numbers up to a given count
def generate_triangular_series(count):
    return [n * (n + 1) // 2 for n in range(1, count + 1)]

# Example usage:
print("Triangular Series:", generate_triangular_series(10))


# 8. Pentagonal Numbers Series
# Generates pentagonal numbers up to a given count
def generate_pentagonal_series(count):
    return [n * (3 * n - 1) // 2 for n in range(1, count + 1)]

# Example usage:
print("Pentagonal Series:", generate_pentagonal_series(10))


# 9. Hexagonal Numbers Series
# Generates hexagonal numbers up to a given count
def generate_hexagonal_series(count):
    return [n * (2 * n - 1) for n in range(1, count + 1)]

# Example usage:
print("Hexagonal Series:", generate_hexagonal_series(10))


# 10. Square Numbers Series
# Generates square numbers up to a given count
def generate_square_series(count):
    return [n ** 2 for n in range(1, count + 1)]

# Example usage:
print("Square Series:", generate_square_series(10))


# 11. Cube Numbers Series
# Generates cube numbers up to a given count
def generate_cube_series(count):
    return [n ** 3 for n in range(1, count + 1)]

# Example usage:
print("Cube Series:", generate_cube_series(10))


# 12. Happy Numbers Series
# Checks if a number is a happy number
def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

# Generates a list of happy numbers up to a limit
def generate_happy_series(limit):
    return [num for num in range(1, limit) if is_happy(num)]

# Example usage:
print("Happy Series:", generate_happy_series(50))


# 13. Harshad (Niven) Numbers Series
# Checks if a number is a Harshad number
def is_harshad(num):
    return num % sum(int(digit) for digit in str(num)) == 0

# Generates a list of Harshad numbers up to a limit
def generate_harshad_series(limit):
    return [num for num in range(1, limit) if is_harshad(num)]

# Example usage:
print("Harshad Series:", generate_harshad_series(50))


# 14. Bell Numbers Series
# Generates Bell numbers up to a given count using dynamic programming
def generate_bell_series(count):
    bell = [[0 for i in range(count)] for j in range(count)]
    bell[0][0] = 1
    for i in range(1, count):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i + 1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return [bell[i][0] for i in range(count)]

# Example usage:
print("Bell Series:", generate_bell_series(10))


# 15. Tetrahedral Numbers Series
# Generates tetrahedral numbers up to a given count
def generate_tetrahedral_series(count):
    return [n * (n + 1) * (n + 2) // 6 for n in range(1, count + 1)]

# Example usage:
print("Tetrahedral Series:", generate_tetrahedral_series(10))