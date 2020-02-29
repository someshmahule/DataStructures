class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CircularList:

    def __init__(self,head):
        self.head = head
        self.head.next = self.head

    
    def push(self,data):
        tail = Node(data)
        if self.head:
            itr = self.head
            while(itr):
                if itr.next == self.head:
                    break
                itr = itr.next
            itr.next = tail
            tail.next = self.head

    def printList(self):
        if self.head:
            itr = self.head.next
            while(itr!= None and itr != self.head):
                print(itr.data)
                itr = itr.next
            return

def main():

    blk = Node(0)
    obj = CircularList(blk)
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.printList()

if __name__ == "__main__":
    main()





