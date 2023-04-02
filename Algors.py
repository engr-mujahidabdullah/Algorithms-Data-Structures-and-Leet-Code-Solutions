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

    def bubble(self, list_s : list, acc = True):
        for i in range(len(list_s)):
            for j in range(0, len(list_s) - i -1):
                if( acc == True):
                    if(list_s[j] > list_s[j + 1]):
                        list_s[j + 1], list_s[j] = list_s[j], list_s[j+1]
                else:
                    if(list_s[j] < list_s[j + 1]):
                        list_s[j + 1], list_s[j] = list_s[j], list_s[j+1]    
        self.list_sorted = list_s



test = Algors()
test.bubble([3,10,5,1,7], acc = False)
print(test.list_)