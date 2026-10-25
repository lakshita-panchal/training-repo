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


# --- Example Usage ---
print("--- Stack Demo ---")
my_stack = Stack()
my_stack.push("Book A")
my_stack.push("Book B")
my_stack.push("Book C")

print(f"Top item (peek): {my_stack.peek()}")
print(f"Popped: {my_stack.pop()}")
print(f"Popped: {my_stack.pop()}")
print(f"Is stack empty? {my_stack.is_empty()}")

