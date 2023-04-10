class Queue:
    def __init__(self, elements = None):
      if(elements == None):
        self.elements = list()
      else:
        self.elements = elements
    
    def enqueue(self, item):
        self.elements.append(item)
    
    def dequeue(self):
      if(len(self.elements) > 0):
        return self.elements.pop(0)
      
    def get_first(self):
      if(len(self.elements) > 0):
        return self.elements[0]
      
    def get_last(self):
      if(len(self.elements) > 0):
        return self.elements[-1]
    
    def get_size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0
      
    def __str__(self):
        return str(self.elements)

if __name__ == "__main__":
    import numpy as np
    event = "0IO00000IO000000IIOOI0000000000000O00000000000000000000000000000000IOIO000000000000000IO000IO0000000000000I0OIO0000000000I000II0O00O000000000I0O0O0000I0I0000000III00000OO000000000O000000O0I000000000000000I0O0O0000O00000000000000000000000000000000000000000IO0000000000000000IO000000000000IO0000000IO00IO000000I00O00000000I00000IO000IIO000000O00O0000I00000I00000O000O00000I00O00000IO0000000000000000000IO00000000000000000000000IO000IIOO0000000000000000000000000000000IIOO000000"
    time = []
    cont = [0,0,0]
    for i in range(len(event)):
        if(event[i] == "R"):
            cont[0] = cont[0] + 1
            time.append(1)
        #if(event[i] == "0"):
        #    pass
        if(event[i] == "I"):
            cont[1] = cont[1] + 1
            for j in range(i, len(event)):
                if(event[j] == "O"):
                    cont[2] = cont[2] + 1
                    time.append((j - i))
                    event.replace(event[j],"0")
                    break
        #if(event[i] == "O"):
        #    pass
    print(len(event))
    print(cont)
    print(time)
    print(len(time))
    print(np.mean(time))
