"""
I know this is not efficient
"""
import sys
sys.path.append("../LinkedList")
from Singly_LinkedList.singly_ll import SinglyLinkedList, Node
class Stack:
    def __init__(self) -> None:
        self.items = SinglyLinkedList()
    def is_empty(self):
        return self.items.head is None
    def push(self,item):
        self.items.append(item)
    def pop(self):
        """Not so Good Approch"""
        if self.is_empty():
            return IndexError("[-]Stack is Empty: Can't pop")
        current = self.items.head
        last = self.items.head
        while current:
            last =  current
            current = current.next
        data = last.data
        current = self.items.head
        prev = None
        while id(current) != id(last):
            prev = current
            current = current.next
        last = None
        prev.next = None
        return data
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())

    # print("Top element:", stack.peek())
    # print("Size of stack:", stack.size())
    print("Is stack empty?", stack.is_empty())