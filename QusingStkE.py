from SimpleStk import Stk

class Que :

    def __init__(self,size):
        self.size = size
        self.stk1 = Stk(self.size)
        self.stk2 = Stk(self.size)

    def enq(self,x):
        if self.stk1.isEmpty() == "Empty":
            self.stk1.push(x)
        else:
            while(self.stk1.isEmpty()!= "Empty"):
                p = self.stk1.pop()
                self.stk2.push(p)
            self.stk1.push(x)
            while(self.stk2.isEmpty() != "Empty"):
                x = self.stk2.pop()
                self.stk1.push(x)

    def deq(self):
        if self.stk1.isEmpty() == "Empty":
            print("Queue is Empty")
            return
        else:
            return self.stk1.pop()

    def printQ(self):
        self.stk1.printStk()
    
if __name__ == "__main__":
    a = Que(4)
    a.enq(1)
    a.enq(2)
    a.enq(3)
    a.enq(4)
    a.enq(5)
    a.printQ()
    a.deq()
    a.deq()
    a.printQ()