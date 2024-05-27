class Stack:
    def __init__(self) -> None:
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return IndexError("[-]Stack is Empty: Can't pop")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return IndexError("[-]Stack is Empty: Can't Peek")
        return self.items[-1]
    def size(self):
        return len(self.items)
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print("Popped:", stack.pop())
    print("Top element:", stack.peek())
    print("Size of stack:", stack.size())
    print("Is stack empty?", stack.is_empty())