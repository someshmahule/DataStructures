#
#   Code To Learn Link List Operations
#   
#   -Somesh Mahule
#

class Node():

    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkList():

    def __init__(self, head) :
        self.head = head

    
    #function to Print List
    def printList(self):
        start = self.head
        while(start):
            print(start.data)
            start = start.next

    #Function to Add Node into a Link List
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

    #Function to Add Node at start of Link List
    def addAtStart(self, data):
        top = Node(data)
        if self.head == None:
            self.head = top
            return
        tmp = self.head
        self.head = top
        top.next = tmp

    #Function to Check if Link List exist
    def isList(self):
        if self.head == None:
            return False
        else:
            return True

    #Fucntion to Delete Head Of a Link List
    def delHead(self):
        if self.isList():
            tmp = self.head
            self.head = tmp.next
            return
        else:
            print("Empty List")

    #Function to Delete Node Particular Position
    def delI(self, ind):
        i=0
        if self.isList():
            if ind == 0:
                self.delHead()
                return
            start = self.head
            while(i!=ind):
                i = i+1
            tmp = start.next
            start.next = tmp.next
            start = start.next
    
    #Function to Delete Node of a Particular Key
    def delKey(self, key):
        if self.isList():
            if key == self.head.data :
                return self.delHead()
            else:
                itr = self.head
                while (itr.next.data != key) :
                    itr = itr.next
                tmp = itr.next
                itr.next = tmp.next

    #Function to Delete Whole Link List
    def delList(self):
        self.head = None
        return

    #Function to Get Length of Link List
    def getLength(self):
        if self.isList() == False:
            return 0
        else:
            l = 0
            itr = self.head
            while(itr):
                itr = itr.next
                l = l+1
            return l

    def searchKey(self,key):
        if self.isList():
            itr = self.head
            while(itr.next!=None and itr.data != key):
                itr = itr.next
            if itr.next == None:
                return False
            else:
                return True

    def getNthNode(self, n):
        if self.isList():
            itr = self.head
            i=0
            while(i!=n):
                itr = itr.next
                i = i+1
            return itr.data

#Driver Fucntion for Link List Operations
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
    ll.delI(1)
    print("After Delete")
    ll.printList()
    ll.delKey(0)
    print("After Delete")
    ll.printList()
    print("Length of List ",ll.getLength())
    ll.printList()
    print("Enter key to Search")
    key = int(input())
    print(ll.searchKey(key))
    print("Give Nth Node to Search")
    n = int(input())
    print("Nth Node is ",ll.getNthNode(n))
    ll.delList()
    print("After Link List Delete")


if __name__ == "__main__":
    main()
