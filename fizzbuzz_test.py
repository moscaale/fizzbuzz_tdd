import unittest

from fizzbuzz import fizzbuzz


class MyTestCase(unittest.TestCase):
    def test_fizzbuzz__given_1_return_1(self):
        # Given
        expected = 1
        input_value = 1
    
        # When
        actual = fizzbuzz(input_value)
    
        # Then
        assert actual == expected

    def test_fizzbuzz_given_2_return_2(self):
        # Given
        expected = 2
        input_value =2
        # When
        actual = fizzbuzz(input_value)
        # Then
        assert actual == expected

    def test_fizzbuzz__given_3_return_fizz(self):
        # Given
        expected = "fizz"
        input_value = 3

        # When
        actual = fizzbuzz(input_value)

        # Then
        assert actual == expected

    def test_fizzbuzz__given_4_return_4(self):
        # Given
        expected = 4
        input_value = 4

        # When
        actual = fizzbuzz(input_value)

        # Then
        assert actual == expected

    def test_fizzbuzz_given_5_return_buzz(self):
        # Given
        expected = 'buzz'
        input_value = 5

        # When
        actual = fizzbuzz(input_value)

        # Then
        assert actual == expected

    def test_fizzbuzz_given_6_return_fizz(self):
        # Given
        expected = "fizz"
        input_value =6
        # When
        actual = fizzbuzz(input_value)
        # Then
        assert actual == expected

    def test_fizzbuzz__given_10_return_buzz(self):
        # Given
        expected = "buzz"
        input_value = 10
        # When
        actual = fizzbuzz(input_value)
        # Then
        assert actual == expected






    

if __name__ == '__main__':
    unittest.main()
