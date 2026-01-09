import unittest
from greet import greet


class TestGreet(unittest.TestCase):
    """Test cases for the greet function."""

    def test_greet_with_name(self):
        """Test that greet returns the correct greeting message."""
        result = greet("World")
        self.assertEqual(result, "Hello, World!")

    def test_greet_with_different_name(self):
        """Test greet with a different name."""
        result = greet("Alice")
        self.assertEqual(result, "Hello, Alice!")


if __name__ == "__main__":
    unittest.main()
