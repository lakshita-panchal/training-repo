import unittest
from BasicStack import Stack

class TestStackMethods(unittest.TestCase):
    
    def test_push_increases_size(self):
        """Test 1: Verify pushing items updates stack size appropriately."""
        my_stack = Stack()
        my_stack.push("TestItem")
        self.assertEqual(my_stack.size(), 1)
        self.assertEqual(my_stack.peek(), "TestItem")

    def test_pop_empty_stack_returns_message(self):
        """Test 2: Verify popping from a new stack handles emptiness gracefully."""
        my_stack = Stack()
        result = my_stack.pop()
        self.assertEqual(result, "Stack is empty")

if __name__ == "__main__":
    unittest.main()

