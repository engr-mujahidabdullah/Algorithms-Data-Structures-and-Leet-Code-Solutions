class Stack():

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items
    
    def peek(self):
        if (len(self.items) != 0):
            return self.items[-1]

class node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.next = None

class linkedList:
    def __init__(self):
        self.headval = None

    def atStart(self, val):
        NewNode = node(val)

    def printLinked(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.next
    
    def updateLinked(self, NewNode):
        NewNode.nextval = self.headval
        self.headval = NewNode

class Algors:

    def __init__(self):
        self.int1 = 0
        self.int2 = 0
        self.list_sorted = []
        pass

    def swap(self, int1 : int, int2 : int):
        int1 = int1 + int2
        int2 = int1 - int2
        int1 = int1 - int2
        self.int1 = int1
        self.int2 = int2
        return int1, int2

    def bubble(self, list_s : list, acc = True):
        for i in range(len(list_s)):
            for j in range(0, len(list_s) - i -1):
                if( acc == True):
                    if(list_s[j] > list_s[j + 1]):
                        list_s[j], list_s[j + 1] = self.swap(list_s[j], list_s[j + 1])
                else:
                    if(list_s[j] < list_s[j + 1]):
                        list_s[j], list_s[j + 1] = self.swap(list_s[j], list_s[j + 1])
        self.list_sorted = list_s

    def insertion(self, list_s : list, acc = True):
        for i in range(1, len(list_s)):
            j = i
            if( acc == True):
                while (j > 0 and list_s[j - 1] > list_s[j]):
                    list_s[j], list_s[j - 1] = self.swap(list_s[j], list_s[j - 1])
                    j -= 1
            if( acc == False):
                while (j > 0 and list_s[j - 1] < list_s[j]):
                    list_s[j], list_s[j - 1] = self.swap(list_s[j], list_s[j - 1])
                    j -= 1
        
        self.list_sorted = list_s



test = linkedList()
test.headval = node("Alpha")
a1 = node("Beta")
a2 = node("charlie")
a3 = node("delta")
test.headval.next = a1
a1.next = a2
a2.next = a3

test.printLinked()
