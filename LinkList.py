class Node():

    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkList():

    def __init__(self, head) :
        self.head = head

    def printList(self):
        start = self.head
        while(start):
            print(start.data)
            start = start.next

    def add(self, data):
        if self.head == None:
            top = Node(data)
            self.head = top
            return
        start = self.head
        while(start.next):
            start = start.next
        tail = Node(data)
        start.next = tail

    def addAtStart(self, data):
        top = Node(data)
        if self.head == None:
            self.head = top
            return
        tmp = self.head
        self.head = top
        top.next = tmp
            

def main():
    a = Node(1)
    ll = LinkList(a)
    #ll.printList()
    ll.add(2)
    ll.add(3)
    print("LinkList\n")
    ll.printList()
    ll.addAtStart(0)
    print("LinkList\n")
    ll.printList()

if __name__ == "__main__":
    main()
