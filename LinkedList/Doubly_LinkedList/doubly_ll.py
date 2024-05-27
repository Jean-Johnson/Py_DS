class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    def prepend(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next =self.head
        self.head.prev = new_node
        self.head = new_node
    def remove(self,key):
        current = self.head
        while current:
            if current.data == key and current == self.head:
                if not current.next:
                    current = self.head = self.tail = None
                    return
                else:
                    next_node = current.next
                    current.next = next_node.prev = None
                    current = None
                    self.head = next_node
                    return
            elif current.data == key:
                if current.next:
                    next_node = current.next
                    prev_node = current.prev
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    # deleting
                    current.next = current.prev = None
                    current = None
                    return
                else:
                    prev_node = current.prev
                    prev_node.next = None
                    current.prev = None
                    current = None
                    self.tail = prev_node
                    return
            current = current.next
    def __reversed__(self) -> str:
        out_string = "[ "
        current = self.tail
        while current:
            out_string += f"{current.data} => "
            current = current.prev
        out_string += "None ]"
        return out_string
    def __str__(self) -> str:
        out_string = "[ "
        current = self.head
        while current:
            out_string += f"{current.data} => "
            current = current.next
        out_string += "None ]"
        return out_string
    

if __name__=="__main__":
    LL = DoublyLinkedList()
    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)
    LL.append(5)
    print(f"After Appending {LL}")
    LL.prepend(0)
    LL.prepend(-1)
    print(f"After Prepending {LL}")
    LL.remove(3)
    print(f"After Removing 3 {LL}")
    print(f"Reverse Traverse {reversed(LL)}")