import unittest

def numbers_to_roman(number):
    dictionary = { 
        'ones' : {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'},
        'tens' : {10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC'},
        'hundreds': {100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM'},
        'thousands': {1000: 'M', 2000: 'MM', 3000: 'MMM'}
    }

    result = ''
    for magnitude, category in zip([1000, 100, 10, 1], ['thousands', 'hundreds', 'tens', 'ones']):
        digit = (number // magnitude) * magnitude
        if digit > 0:
            result += dictionary[category][digit]
        number %= magnitude

    return result


def roman_to_numbers(roman):
    dictionary = {
        'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
        'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90,
        'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500, 'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900,
        'M': 1000, 'MM': 2000, 'MMM': 3000
    }

    result = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i+2] in dictionary:
            result += dictionary[roman[i:i+2]]
            i += 2
        else:
            result += dictionary[roman[i]]
            i += 1

    return result
        

# Tests for numbers_to_roman
class number_test(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(numbers_to_roman(4), 'IV')

    def test_double_digit(self):
        self.assertEqual(numbers_to_roman(50), 'L')

    def test_triple_digit(self):
        self.assertEqual(numbers_to_roman(123), 'CXXIII')

    def test_quad_digit(self):
        self.assertEqual(numbers_to_roman(1993), 'MCMXCIII')

# Test for roman_to_numbers
class roman_test(unittest.TestCase):
    def test_I(self):
        self.assertEqual(roman_to_numbers('V'), 5)

    def test_X(self):
        self.assertEqual(roman_to_numbers('XLV'), 45)

    def test_C(self):
        self.assertEqual(roman_to_numbers('XLV'), 45)

    def test_M(self):
        self.assertEqual(roman_to_numbers('MMXXIV'), 2024)

if __name__ == '__main__':
    unittest.main()