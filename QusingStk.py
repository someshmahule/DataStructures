from SimpleStk import Stk

class Que:

    def __init__(self,size):
        self.size = size
        self.stk1 = Stk(self.size)
        self.stk2 = Stk(self.size)

    def enq(self,x):
        self.stk1.push(x)

    def deq(self):
        if self.stk1.isEmpty() == "Empty":
            print("Queue is empty")
            return
        while(self.stk1.isEmpty()!= "Empty"):
            x = self.stk1.pop()
            self.stk2.push(x)
        
        ret = self.stk2.pop()
        while(self.stk2.isEmpty()!="Empty"):
            x = self.stk2.pop()
            self.stk1.push(x)
        return ret

    def printQ(self):
        self.stk1.printStk()

if __name__ == "__main__":
    a = Que(5)
    a.enq(1)
    a.enq(2)
    a.enq(3)
    a.printQ()
    a.deq()
    a.deq()
    a.enq(4)
    a.enq(5)
    a.deq()
    #a.deq()
    a.printQ()
