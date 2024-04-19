class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkList:
    def __init__(self,value) -> None:
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value=value)
        if self.length == 0:
            
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length = +1
        return True
    

l = LinkList(6)
l.append(7)
l.print_list()