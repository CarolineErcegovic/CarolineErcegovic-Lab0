"""Tests for Lab 0 Question 1"""

import sys
sys.path.append(".")
import unittest
from src.q1 import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_true(self):
        self.assertEqual(is_palindrome("racecar"), True)

    def test_false(self):
        self.assertEqual(is_palindrome("hello"), False)