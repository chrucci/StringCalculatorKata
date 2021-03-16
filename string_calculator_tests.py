import unittest
import string_calculator as calc
from invalid_addend_exception import InvalidAddnedException


class StringCalculatorTests(unittest.TestCase):
    def test_add__with_empty_string__returns_zero(self):
        expected = 0
        actual = calc.add("")
        self.assertEqual(expected, actual)

    def test_add__with_zero__returns_zero(self):
        expected = 0
        actual = calc.add("0")
        self.assertEqual(expected, actual)

    def test_add__with_one__returns_one(self):
        expected = 1
        actual = calc.add("1")
        self.assertEqual(expected, actual)

    def test_add__with_two__returns_two(self):
        expected = 2
        actual = calc.add("2")
        self.assertEqual(expected, actual)

    def test_add__with_one_and_two__returns_sum(self):
        expected = 3
        actual = calc.add("1,2")
        self.assertEqual(expected, actual)

    def test_add__with_a_dozen_numbers__returns_sum(self):
        expected = 78
        actual = calc.add("1,2,3,4,5,6,7,8,9,10,11,12")
        self.assertEqual(expected, actual)

    def test_add__with_one_and_two__newline_seperator__returns_sum(self):
        expected = 3
        actual = calc.add("""1
        2""")
        self.assertEqual(expected, actual)

    def test_add__with_one_and_two__with_mixed_separators__returns_sum(self):
        expected = 6
        actual = calc.add("1,2\n3")
        self.assertEqual(expected, actual)

    def test_add__with_custom_separator__returns_sum(self):
        expected = 6
        actual = calc.add("//;\n1;2;3")
        self.assertEqual(expected, actual)

    def test_add__with_only_one_negative_num__throws_exception(self):
        with self.assertRaises(InvalidAddnedException) as e:
            calc.add("-1")
        self.assertEqual(e.exception.args[0], "Negative numbers are not allowed.  You included '-1'")

    def test_add__with_one_negative_num__throws_exception(self):
        with self.assertRaises(InvalidAddnedException) as e:
            calc.add("1,-1")
        self.assertEqual(e.exception.args[0], "Negative numbers are not allowed.  You included '-1'")

    def test_add__with_two_negative_nums__throws_exception(self):
        with self.assertRaises(InvalidAddnedException) as e:
            calc.add("1,-1,3,-2")
        self.assertEqual(e.exception.args[0], "Negative numbers are not allowed.  You included '-1,-2'")


if __name__ == '__main__':
    unittest.main()
