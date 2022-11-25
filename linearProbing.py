class LinearProbingHash:

    # This is a single record in a chaining hash table.  You can
    # change this in anyway you wish (including not using it at all)
    class Record:
        def __init__(self, key = None, value=None):
            self.key = key
            self.value = value

    # You cannot change the function prototypes below.  Other than that
    # how you implement the class is your choice (but it must be a hash
    # table that use linear probing for collision resolution)
    
    def __init__(self, cap=32):
        self.cap = cap
        self.arr = [None for i in range(cap)] 
        self.size = 0

    def insert(self,key, value):
        if (self.search(key)!=None):#check if key already exists
            return False

        index= self.hash(key)

        for i in range(index, self.cap*2):
            if self.arr[i % self.cap] == None:
                self.arr[i % self.cap] = self.Record(key,value)
                self.size+=1
                break
        if(self.size >= (self.cap * 0.7)):
            self.resize()

        return True
    def modify(self, key, value):
        index= self.hash(key)

        for i in range(index, self.cap*2):
            if self.arr[i % self.cap] != None and self.arr[i % self.cap].key == key:
                self.arr[i % self.cap].value = value
                return True
        
        return False

    def remove(self, key):
        index = self.hash(key) 

        for i in range(index, self.cap*2): 
            if self.arr[i % self.cap] != None and self.arr[i % self.cap].key == key:
                self.arr[i % self.cap] = None
                self.size-=1
                return True
        
        return False

    def search(self, key):
        index = self.hash(key) 
        for i in range(index, self.cap*2): 
            if self.arr[i % self.cap] != None and self.arr[i % self.cap].key == key:
                return self.arr[i % self.cap].value

        return None
    def capacity(self):
        return self.cap

    def __len__(self):
        return self.size

    def resize(self):
        temp = [None for i in range(self.cap*2)]
        for i in range(self.cap):
            temp[i]=self.arr[i]
        self.arr = temp
        self.cap *= 2	

    def hash(self,key):
        return hash(key) % self.cap
