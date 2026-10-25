import argparse

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return the top item of the stack."""
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        """View the top item without removing it."""
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)


if __name__ == "__main__":
    # 1. Set up argparse configuration
    parser = argparse.ArgumentParser(description="CLI interface for Basic Stack Operations.")
    parser.add_argument(
        "--push", 
        type=str, 
        help="Provide a string item to push onto the stack from the command line."
    )
    args = parser.parse_args()

    # 2. Conditional logic based on terminal input
    if args.push:
        print("--- CLI Execution ---")
        my_stack = Stack()
        my_stack.push(args.push)
        print(f"Current top item: {my_stack.peek()}")
    else:
        # Fallback to your original demo if no CLI args are given
        print("--- Stack Demo ---")
        my_stack = Stack()
        my_stack.push("Book A")
        my_stack.push("Book B")
        my_stack.push("Book C")

        print(f"Top item (peek): {my_stack.peek()}")
        print(f"Popped: {my_stack.pop()}")
        print(f"Popped: {my_stack.pop()}")
        print(f"Is stack empty? {my_stack.is_empty()}")

