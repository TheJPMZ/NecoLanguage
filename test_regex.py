from unittest import TestCase
from regex import check_regex, to_postfix, transform

class TestCheckRegex(TestCase):
    def test_invalid_regex_empty(self):
        with self.assertRaises(ValueError):
            check_regex("")

    def test_invalid_regex_operator1(self):
        with self.assertRaises(ValueError):
            check_regex("|abc")

    def test_invalid_regex_operator2(self):
        with self.assertRaises(ValueError):
            check_regex("abc|")

    def test_invalid_regex_parenthesis1(self):
        # Test if the regex contains an unopened parenthesis
        with self.assertRaises(ValueError):
            check_regex("a)b")

    def test_invalid_regex_parenthesis2(self):
        with self.assertRaises(ValueError):
            check_regex("(a")

    def test_invalid_regex_parenthesis3(self):
        with self.assertRaises(ValueError):
            check_regex("()")

    def test_invalid_regex_stutter(self):
        with self.assertRaises(ValueError):
            check_regex("a**")

    def test_valid_regex1(self):
        regex = "a|b.c*|d+"
        self.assertTrue(check_regex(regex))

    def test_valid_regex2(self):
        regex = "(A|ε)*|B(A+)C?|D"
        self.assertTrue(check_regex(regex))

    def test_valid_regex3(self):
        regex = "0? (1?)? 0 *"
        self.assertTrue(check_regex(regex))

class TestExplicit(TestCase):
    def test_explicit1(self):
        regex = "abc"
        self.assertEqual(transform(regex), "a.b.c")
        self.assertTrue(check_regex(transform(regex)))

    def test_explicit2(self):
        regex = "(a|b)c*|d+"
        self.assertEqual(transform(regex), "(a|b).c*|d+")
        self.assertTrue(check_regex(transform(regex)))

    def test_explicit3(self):
        regex = "ab+c"
        self.assertEqual(transform(regex), "a.b+.c")
        self.assertTrue(check_regex(transform(regex)))


class TestToPostfix(TestCase):
    def test_postfix1(self):
        regex = "a.b+.c"
        self.assertEqual(to_postfix(regex), "ab+.c.")

    def test_postfix2(self):
        regex = "(A|ε)*|B(A+)C?|D"
        self.assertEqual(to_postfix(regex), "Aε|*BA+C?|D|")

    def test_postfix3(self):
        regex = "a.(b.b)+.c"
        self.assertEqual(to_postfix(regex), "abb.+.c.")

class TestIntegrated(TestCase):
    def test_regex1(self):
        regex = "abc"
        regex = transform(regex)
        self.assertTrue(check_regex(regex))
        self.assertEqual(to_postfix(regex), "ab.c.")

    def test_regex2(self):
        regex = "(a*|b*).c"
        regex = transform(regex)
        self.assertTrue(check_regex(regex))
        self.assertEqual(to_postfix(regex), "a*b*|c.")

    def test_regex3(self):
        regex = "a(bb)+c"
        regex = transform(regex)
        self.assertTrue(check_regex(regex))
        self.assertEqual(to_postfix(regex), "abb.+.c.")





