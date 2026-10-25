class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the first item of the queue."""
        if self.is_empty():
            return "Queue is empty"
        # pop(0) removes the element at index 0
        return self.queue.pop(0)

    def peek(self):
        """View the front item without removing it."""
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)


# --- Example Usage ---
print("\n--- Queue Demo ---")
my_queue = Queue()
my_queue.enqueue("Customer 1")
my_queue.enqueue("Customer 2")
my_queue.enqueue("Customer 3")

print(f"Front item (peek): {my_queue.peek()}")
print(f"Dequeued: {my_queue.dequeue()}")
print(f"Dequeued: {my_queue.dequeue()}")
print(f"Queue size: {my_queue.size()}")

