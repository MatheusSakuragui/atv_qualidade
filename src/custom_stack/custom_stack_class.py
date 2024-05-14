class StackEmptyException(Exception):
    pass

class StackFullException(Exception):
    pass

class CustomStack:

    def __init__(self, pLimit):
        self.limit = pLimit
        self.elements = []
    
    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.size() == 0

    def push(self, element):
        if self.size() == self.limit:
            raise StackFullException("Stack is full")
        self.elements.append(element)
    
    def pop(self):
        if self.isEmpty():
            raise StackEmptyException("Stack is empty")
        return self.elements.pop()
    
    def top(self):
        if self.isEmpty():
            raise StackEmptyException("Stack is empty")
        return self.elements[-1]
