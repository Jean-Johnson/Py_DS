class Node:
    def __init__(self,data) -> None:
        """
        stores the data and the pointer to next node
        """
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        """
        New nodes get added to head
        """
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def remove(self,key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def __str__(self) -> str:
        out_string = "[ "
        current = self.head
        while current:
            out_string += f"{current.data} => "
            current = current.next
        out_string += "None ]"
        return out_string
    
if __name__=="__main__":
    LL = SinglyLinkedList()
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