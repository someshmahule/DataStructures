class Stk:
    def __init__(self,size):
        self.size = size
        self.stk = []
    
    def printStk(self):
        print(self.stk)
    
    def isEmpty(self):
        if len(self.stk) == 0:
            return "Empty"
        else:
            return "Not Empty"

    def push(self,x):
        self.stk.append(x)

    def pop(self):
        l = len(self.stk) - 1
        x = self.stk[l]
        self.stk = self.stk[:l]
        return x

    def isOverflow(self):
        if len(self.stk) == self.size :
            return "Overflown"
        else:
            return "Not Overflown"
    
if __name__ == "__main__":
    
    a = Stk(3)
    #a.printStk()
    print(a.isEmpty())
    a.push(1)
    a.push(2)
    a.push(3)
    print(a.isOverflow())
    a.printStk()
    print(a.pop())
    print(a.pop())
    a.printStk()