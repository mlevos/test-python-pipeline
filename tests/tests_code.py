import unittest
from src.code import MyClass


class TestMyClass(unittest.TestCase):
    """Classe de test"""
    def test_get_name(self):
        """ Test """
        test_object = MyClass("Test")
        self.assertEqual(test_object.get_name(), "Test")
