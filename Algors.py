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

    """
    Build Array from Permutation
    Given a zero-based permutation nums (0-indexed), build an array ans of the same length
    where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it. A zero-based
    permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
    """
    def buildArray(self, nums: list[int]) -> list[int]:
        out = []
        for i in range(len(nums)):
            out.append(nums[nums[i]])
        return out

    """
    You are given a positive integer num consisting only of digits 6 and 9.
    Return the maximum number you can get by changing at most one digit 
    (6 becomes 9, and 9 becomes 6).
    """
    def maximum69Number (self, num: int) -> int:
        ans = num
        num =str(num)
        numx = num
        for i in range(len(num)):
            numx = num
            if(num[i] == '6'):
                numx = numx[:i] + '9' + numx[i+1:]
                print(numx)
            else:
                numx = numx[:i] + '6' + numx[i+1:]
            print(numx[i])
            if(int(numx) >= ans):
                ans = int(numx)
        return ans

    """
    Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
    """
    def smallestEvenMultiple(self, n: int) -> int:
        mul = []
        ans = 0
        for i in range(1,n+1):
            ans = i * 2
            if(ans%n == 0 and ans%2 == 0):
                mul.append(ans)
        return(min(mul))

    """
    Given two positive integers a and b, return the number of common factors of a and b.
    An integer x is a common factor of a and b if x divides both a and b.
    """
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        for i in range(1,min(a,b) + 1):
            if(a%i == 0 and b%i == 0):
                count = count + 1
        return count

    def commonFactorsList(self, a: int, b: int) -> list:
        fact = []
        for i in range(1,min(a,b) + 1):
            if(a%i == 0 and b%i == 0):
                fact.append(i)
        return fact

    def is_prime(self, n):
        for i in range(2,int(n/2) + 1):
            if(n%i == 0):
                return False
        return True

    def countPrimes(self, n: int) -> int:
        if (n == 0 or n == 1):
            return 0
        count = 0
        for i in range(2,n):
            if(self.is_prime(i) == True):
                count = count + 1
        return count


if __name__ == "__main__":
    test = Algors()
    #print(test.is_empty())
    print(test.commonFactorsList(256, 512))
    #test.parenthesis_Balance("{()}")