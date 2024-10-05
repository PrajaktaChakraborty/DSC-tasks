class ArrayStack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from an empty stack")
    def is_empty(self):
        return len(self.stack) == 0
    
array_stack = ArrayStack()
array_stack.push(10)
array_stack.push(20)
print(array_stack.peek())
print(array_stack.pop())
print(array_stack.pop())