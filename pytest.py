import unittest

# This is the function or class you want to test
def add_numbers(a, b):
    return a + b

class Pytest(unittest.TestCase):
    """
    A test class for the add_numbers function.
    """

    def test_positive_numbers(self):
        """
        Tests adding two positive numbers.
        """
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()
