import unittest

# This is the function or class you want to test
def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    """
    A test class for the add_numbers function.
    """

    def test_positive_numbers(self):
        """
        Tests adding two positive numbers.
        """
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)

    def test_negative_numbers(self):
        """
        Tests adding two negative numbers.
        """
        result = add_numbers(-5, -3)
        self.assertEqual(result, -8)

    def test_mixed_numbers(self):
        """
        Tests adding a positive and a negative number.
        """
        result = add_numbers(5, -3)
        self.assertEqual(result, 2)

    def test_zero(self):
        """
        Tests adding a number with zero.
        """
        result = add_numbers(7, 0)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
