import _collections_abc
import numbers
from math import log, ceil


class BasicMaths:
    def __init__(self) -> None:
        pass

    ## Count all digits of a number
    def count_all_digits_of_a_number(self, number):
        counter = 0
        while number > 0:
            # number = number / 10
            number = number // 10
            # print(number)
            counter += 1
        return counter


    # Time Complexity -> O(1)
    def count_all_digits_of_a_number_using_log(self, number):
        counter = int(log(number, 10))+1
        return counter

    ## Count number of odd digits in a number
    def count_number_of_odd_digits_in_a_number(self, number):
        counter = 0
        while number > 0:
            digit = number % 10
            number = number // 10
            if digit % 2 != 0:
                counter += 1
        return counter


    # Reverse a number
    def reverse_a_number(self, number):
        new_number = 0
        while number > 0:
            digit = number % 10
            new_number = new_number * 10 + digit
            number = number // 10

        return new_number

    # Palindrome number
    # 121 == 121
    # 123 != 321
    def palindrome_number(self, number):
        copy_number = number
        reversed_number = 0
        # print(copy_number)
        while number > 0 :
            digit = number % 10
            number = number // 10
            reversed_number = reversed_number * 10 + digit
        # print(reversed_number)
        return reversed_number == copy_number

    # Return the largest digit in a number
    def return_the_largest_digit_in_a_number(self, number):
        largest_number = -1
        while number > 0:
            digit = number % 10
            if digit > largest_number :
                largest_number = digit
            number = number // 10
        return largest_number

    # Factorial of a given number
    # 5! = 5 * 4 * 3 * 2 * 1 = 120
    def factorial_of_a_given_number(self, number):
        factors_total = 1
        while number > 0:
            factors_total = factors_total * number
            number -= 1
        return factors_total


    def calculate_power_plus_sum(self, number):
        number_of_digits = self.count_all_digits_of_a_number(number)
        armstrong_number = 0

        while number > 0:
            digit = number % 10
            number = number // 10
            armstrong_number = armstrong_number + (digit ** number_of_digits)
        return armstrong_number


    # Check if the number is armstrong
    # 153 is a 3-digit number where 1^3 + 5^3 + 3^3 = 153
    def check_if_the_number_if_armstrong(self, number):
        armstrong_number = self.calculate_power_plus_sum(number)
        return armstrong_number == number

    # Check for perfect number
    # A perfect number is a whole number that equals the sum of its positive proper divisors, not including the number itself. 
    # For example, 6 is perfect because its divisors (1, 2, and 3) add up to 6. The first four are 6, 28, 496, and 8,128
    def find_sum_of_proper_divisors(self, number):
        sum_of_divisors = 0

        for divisor in range(1, number):
            if number % divisor == 0:
                sum_of_divisors += divisor

        return sum_of_divisors

    def check_for_perfect_number(self, number):
        perfect_number_check = self.find_sum_of_proper_divisors(number)
        return perfect_number_check == number

    # Check for prime number
    # A prime number is a whole number greater than 1 that can only be divided evenly by 1 and itself. 
    # For example, 5 can only be divided by 1 and 5, making it prime. Numbers with more than two factors are composite numbers.
    def check_for_prime_number(self, number):
        is_prime = True
        if number in range(1, 4):
            return is_prime
        elif number == 5:
            return is_prime
        else:    
            for value in range(2, number):
                if number % value == 0:
                    is_prime = False
                    break
            return is_prime

    # Count of prime numbers till N
    def count_of_prime_numbers_till_n(self, number):
        counter = 0
        for num in range(number):
            if num %





basic_maths = BasicMaths()

print("Count all digits of a number:")
print(basic_maths.count_all_digits_of_a_number(2200))


print("Count all digits of a number using log:")
print(basic_maths.count_all_digits_of_a_number_using_log(2200))



print("\nNumber of odd digits in a number:")
print(basic_maths.count_number_of_odd_digits_in_a_number(72215245))

print("\nReverse a number:")
print(basic_maths.reverse_a_number(123))

print("\nPalindrome number:")
print(basic_maths.palindrome_number(12345678987654321))

print("\nReturn the largest digit in a number:")
print(basic_maths.return_the_largest_digit_in_a_number(193827495613453521321412))

print("\nFactorial of a given number:")
print(basic_maths.factorial_of_a_given_number(5))

print("\nCheck if the number if armstrong:")
print(basic_maths.check_if_the_number_if_armstrong(153))

print("\nCheck for perfect number:")
print(basic_maths.check_for_perfect_number(28))
print(basic_maths.check_for_perfect_number(8))



print("\nCheck for perfect number Optimized:")
print(basic_maths.check_for_perfect_number_optimized(28))
print(basic_maths.check_for_perfect_number_optimized(8))



print("\nCheck for prime number:")
print(basic_maths.check_for_prime_number(8))
print(basic_maths.check_for_prime_number(7))
print(basic_maths.check_for_prime_number(1))
print(basic_maths.check_for_prime_number(2))
print(basic_maths.check_for_prime_number(3))
print(basic_maths.check_for_prime_number(4))
print(basic_maths.check_for_prime_number(5))
