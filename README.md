# Number Series Generator

This project is a Python-based tool for generating various mathematical number series, including Palindromes, Armstrong numbers, Lucas numbers, and more. Each series is generated through individual functions designed to be efficient, readable, and customizable. Great for students, researchers, and anyone interested in learning more about number patterns!

## Table of Contents
- [Features](#features)
- [Series Overview](#series-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features
- Generate 15 different number series
- Easy-to-use functions with customizable parameters
- Clear and well-documented code for learning and research

## Series Overview
Here's a list of series included in this project:

1. **Palindrome Numbers**: Numbers that read the same forwards and backwards.
2. **Armstrong Numbers**: Numbers that are equal to the sum of their digits each raised to the power of the number of digits.
3. **Lucas Numbers**: Similar to the Fibonacci sequence but starts with 2 and 1.
4. **Fibonacci Numbers**: A sequence where each number is the sum of the previous two numbers.
5. **Perfect Numbers**: Numbers equal to the sum of their divisors (excluding themselves).
6. **Catalan Numbers**: Numbers used in combinatorics for counting various types of structures.
7. **Triangular Numbers**: Numbers that form an equilateral triangle.
8. **Pentagonal Numbers**: Polygonal numbers representing pentagons.
9. **Hexagonal Numbers**: Polygonal numbers representing hexagons.
10. **Square Numbers**: Perfect squares, such as 1, 4, 9, 16, etc.
11. **Cube Numbers**: Perfect cubes, such as 1, 8, 27, 64, etc.
12. **Happy Numbers**: Numbers that eventually reach 1 when iteratively replaced by the sum of the squares of their digits.
13. **Harshad (Niven) Numbers**: Numbers divisible by the sum of their digits.
14. **Bell Numbers**: Numbers representing the number of ways to partition a set.
15. **Tetrahedral Numbers**: Numbers that can form a tetrahedron.

## Installation
Make sure you have Python 3 installed. Clone the repository and install necessary packages (if any):

git clone https://github.com/yourusername/number-series-generator.git
cd number-series-generator

Note: This project doesn't require any external libraries outside of the Python Standard Library.

## Usage
Each series function is self-contained and can be called independently. You can generate any series by specifying a limit or count.

For example, to generate the first 10 Lucas Numbers:

from series_generator import generate_lucas_series
print(generate_lucas_series(10))

## Examples
Here are some examples of generating various series:

from series_generator import (
    generate_palindrome_series, 
    generate_armstrong_series, 
    generate_fibonacci_series,
    generate_square_series
)

# Generate palindromes up to 1000
print("Palindrome Series:", generate_palindrome_series(1000))

# Generate Armstrong numbers up to 1000
print("Armstrong Series:", generate_armstrong_series(1000))

# Generate the first 10 Fibonacci numbers
print("Fibonacci Series:", generate_fibonacci_series(10))

# Generate the first 10 square numbers
print("Square Series:", generate_square_series(10))

Each function includes inline documentation for easy understanding and customization.

## Contributing
Contributions are welcome! Feel free to submit a pull request for any of the following:

- New series functions
- Optimizations
- Code enhancements
- Documentation improvements

Before submitting, ensure that your code follows the existing coding style and includes appropriate comments.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
