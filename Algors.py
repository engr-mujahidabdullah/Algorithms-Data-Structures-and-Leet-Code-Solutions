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

    def is_empty(self):
        if(len(self.items) == 0):
            return True
        else:
            return False

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

    def atEnd(self, val):
        NewNode = node(val)
        if(self.headval is None):
            self.headval = NewNode
            return
        last = self.headval
        while(last.next):
            last = last.next
        last.next = NewNode

    def inBetwwen(self, bwNode, val):
        if(bwNode is None):
            print("The requested Node is not valid")
            return
        NewNode = node(val)
        NewNode.next = bwNode.next
        bwNode.next = NewNode

    def removeNode(self, Node):
        Head = self.headval
        if(Head is not None):
            if(Head.dataval == Node):
                self.headval = Head.next
                Head = None
                return
        while(Head is not None):
            if(Head.dataval == Node):
                break
            prev = Head
            Head  = Head.next
        if(Head == None):
            return

        prev.next = Head.next
        Head = None


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

    def is_closed(self, p1, p2):
        if(p1 == '{' and p2 == '}'):
            return True
        elif(p1 == '(' and p2 == ')'):
            return True
        elif(p1 == '[' and p2 == ']'):
            return True
        else:
            return False

    def parenthesis_Balance(self, paren):
        balanced = True
        s = Stack()

        if(len(paren) % 2 != 0):
            print('Parenthesis are not banaced')
            balanced = False
            return balanced
        for i in range(len(paren)):
            if( paren[i] in "[{(" ):
                s.push(paren[i])
            else:
                if(s.is_empty() == True):
                    balanced = False
                else:
                    top = s.pop()
                    if(self.is_closed(top, paren[i]) == False):
                        balanced = False
        if(s.is_empty and balanced):
            return True
        else:
            return False
    
    def linearSearch(self, find, list_):
        i = 0
        while i in range(len(list_)):
            if(find == list_[i]):
                return i
            i = i + 1
        return False


                

if __name__ == "__main__":
    test = Algors()
    #print(test.is_empty())
    print(test.linearSearch("a", "bfca"))
    #test.parenthesis_Balance("{()}")