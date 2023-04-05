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
        return list_s

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

    def binarySearch(self, find, list_):
        self.insertion(list_)
        list_ = self.list_sorted

        left = 0
        right = len(list_) - 1

        while(left <= right):
            mid = (left + right) // 2
            if(find == list_[mid]):
                return mid
            elif(list_[mid] < find):
                left = mid + 1
            else:
                right = mid + 1
        return False

    def Sqrt_bin(self, x: int) -> int:
        if x < 2:
            return x
        start = 0
        end = x
        mid = (start + end)//2
        while(start <= end):
            if(mid*mid == x):
                return mid
            elif(mid * mid < x):
                start = mid + 1
            else:
                end = mid - 1

    def floorSqrt(self, x: int) -> int:
        if x < 2:
            return x
        i = 1
        ans = 0
        while(ans <= x):
            i = i + 1
            ans = i * i
        return i - 1
    
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        num = sum(d * 10**i for i, d in enumerate(digits[::-1]))
        num = num + 1
        ans = []
        con = str(num)
        for i in con:
            ans.append(int(i))
        return ans

    def convertTemperature(self, celsius: float) -> list[float]:
        return[celsius + 273.15, celsius * 1.80 + 32.00]
    
    """
    Given an array of integers nums, return the number of good pairs.
    A pair (i, j) is called good if nums[i] == nums[j] and i < j.
    """
    def numIdenticalPairs(self, nums: list[int]) -> int:
        pairs = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i] == nums[j] and i < j):
                    pairs = pairs + 1
        return pairs





if __name__ == "__main__":
    test = Algors()
    #print(test.is_empty())
    print(test.floorSqrt(5))
    #test.parenthesis_Balance("{()}")