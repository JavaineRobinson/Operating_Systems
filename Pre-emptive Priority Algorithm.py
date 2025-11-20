
import threading, time
timevariable = 0 #keeps track of time 
processamount = 3   
class  Process: 
    def __init__(self,Pname,PID,bursttime,priority,arrivaltime):
        self.Pname = Pname
        self.PID = PID
        self.bursttime = bursttime 
        self.priority = priority
        self.arrivaltime = arrivaltime
    
    def isProcessed(self):
        return self.bursttime == 0 
        
    def arrivalTimeReached(self):
        return self.arrivaltime == timevariable
        
class MinHeap: 
    def __init__(self,capacity): 
        self.heap = [0] * capacity #array of heap
        self.capacity = capacity
        self.size = 0 #index of keys
        
    def getParentIndex(self,index): 
        return(index - 1) //2 #gets index of element's parent 
    
    def getLeftChildIndex(self,index): 
        return (2 * index) + 1 #gets index of element's left child
    
    def getRightChildIndex(self,index): 
        return (2 * index) + 2 #gets index of element's right child
    
    def hasParent(self,index): #checks if element has parent
        return self.getParentIndex(index) >= 0 
    
    def hasLeftChild(self,index):  #checks if element has left child
        return self.getLeftChildIndex(index) < self.size 
    
    def hasRightChild(self,index):  #checks if element has right child
        return self.getRightChildIndex(index) < self.size 
    
    def parent(self,index): #gets the key of element's parent
        return self.heap[self.getParentIndex(index)]
    
    def leftChild(self,index):#gets the key of element's left child
        return self.heap[self.getLeftChildIndex(index)]
    
    def rightChild(self,index):#gets the key of element's right child
        return self.heap[self.getRightChildIndex(index)]
    
    def isFull(self): #checks if heap is full
        return self.size == self.capacity
    
    def swap(self,index1,index2): #swaps keys to different indexes
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
        
    def insert(self,process): #inserts element into heap
        if(self.isFull()):
            raise Exception("Heap is Full")
        self.heap[self.size] = process 
        self.size += 1
        self.heapifyUp(self.size - 1)
    
    def heapifyUp(self,index): #places the newly added element into its correct position 
        if(self.hasParent(index) and self.parent(index).priority > self.heap[index].priority):
            self.swap(self.getParentIndex(index),index)
            self.heapifyUp(self.getParentIndex(index))
            
    def removeMin(self): #removes root of minheap
        if(self.size == 0):
            raise Exception("Heap is Empty")
        data = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapifyDown(0) 
        return data 
    
    def heapifyDown(self,index): #resorts the heap after the root is removed
        smallest = index 
        if(self.hasLeftChild(index) and self.heap[smallest].priority > self.leftChild(index).priority): 
            smallest = self.getLeftChildIndex(index)
        
        if(self.hasRightChild(index) and self.heap[smallest].priority > self.rightChild(index).priority): 
            smallest = self.getRightChildIndex(index)
            
        if(smallest != index):
            self.swap(index, smallest)
            self.heapifyDown(smallest)
    
    def printheap(self):
        end = 0 
        while(end < self.size):
            print(self.heap[end].PID, ", ") 
            end += 1 
        
                
            
def it(Mheap): 
    global processamount
    while True: 
        if(Mheap.size > 0): 
            
            if(Mheap.size > 0 and Mheap.heap[0].bursttime > 0):
                Mheap.heap[0].bursttime -= 1 
                print(Mheap.heap[0].Pname, ", ")
            
            if(Mheap.heap[0].bursttime == 0): 
                Mheap.removeMin() 

        else: 
            if(processamount <= 0): 
                break
        
        time.sleep(1)
    
    
    
def keepTime(ProcessArray,Mheap): 
    global timevariable, processamount
    count = 0
    while True: 
        if(ProcessArray[count].arrivalTimeReached()):
            Mheap.insert(ProcessArray[count])
            print(ProcessArray[count].Pname, " is inserted")
            processamount -= 1
            count += 1
            
            if(count == 3):
                break 
            
        time.sleep(1)
        timevariable += 1 
        print("\n Time is: ",timevariable)


if __name__ == "__main__": 
  
    ProcessA = Process("ProcessA",1,10,4,1)
    ProcessB = Process("ProcessB",2,3,5,2)
    ProcessC = Process("ProcessC",3,1,1,4)

    ProcessArray = [0] * processamount 
    ProcessArray[0] = ProcessA
    ProcessArray[1] = ProcessB
    ProcessArray[2] = ProcessC

    Mheap = MinHeap(processamount)


    
    
    thread1 = threading.Thread(target=keepTime, args=(ProcessArray,Mheap), daemon=True)
    thread1.start()
    
    thread2 = threading.Thread(target=it, args=(Mheap, ), daemon=True)
    thread2.start()
   
    #Allows both functions to finish 
    thread1.join()
    thread2.join()
   
    
    
    
    
     
        
    
    
        









        
        
