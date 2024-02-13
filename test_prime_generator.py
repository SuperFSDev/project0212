import unittest
from unittest import mock
from io import StringIO
from prime_generator import prime_generator
import subprocess

class TestPrimeGenerator(unittest.TestCase):

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_main_output(self, mock_stdout):
        start = 1
        end = 10
        expected_output = "Prime numbers in the range 1-10:\n2\n3\n5\n7\n"
        process = subprocess.run(['python', 'main.py', str(start), str(end)], capture_output=True, text=True)
        actual_output = process.stdout
        self.assertEqual(actual_output, expected_output)

    def test_prime_generator(self):
        # Test case 1: Range with prime numbers
        start = 1
        end = 10
        expected_result = [2, 3, 5, 7]
        self.assertEqual(list(prime_generator(start, end)), expected_result)

        # Test case 2: Range with no prime numbers
        start = 24
        end = 28
        expected_result = []
        self.assertEqual(list(prime_generator(start, end)), expected_result)

        # Test case 3: Range with only one prime number
        start = 10
        end = 12
        expected_result = [11]
        self.assertEqual(list(prime_generator(start, end)), expected_result)

        # Test case 4: Range with inverse start and end
        start = 10
        end = 1
        expected_result = [2, 3, 5, 7]
        self.assertEqual(list(prime_generator(start, end)), expected_result)

        # Test case 5: Range with large prime numbers
        start = 7900
        end = 7920
        expected_result = [7901, 7907, 7919]
        self.assertEqual(list(prime_generator(start, end)), expected_result)

if __name__ == '__main__':
    unittest.main()
