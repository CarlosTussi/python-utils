"""
[Class HeapNode]

- Represent a node in the heap.
- It contains a payload/data attribute apart from the key/value.

    Attributes:
    -----------
        value : int
        data : any
"""
class HeapNode():
    
    def __init__(self, value, data = None):
        self.value = value
        self.data = data

    def __str__(self):
        return str(self.value)


"""
[Class Heap]

- Represents a Heap tree where the smallest value has the biggest priority. (min-heap)
- Heap is represented as an array (heapArray)
- This data structure does not provided ordered traversal. Also, it does not allow to locate specific elements or remove specific elements.

    Atttributes:
    ------------
        heapArray : [HeapNode] 

    Methods:
    --------
        insert() - O(log n) - Insert a node in the heap respecting the min-heap property
        delete() - O(log n) - Delete and retrieves a node in the heap respecting the min-heap property
        peek() - O(1) - Retrieves the element with the highest proprtiy without removing it.
        heapSort() - O(n log n) - Sort an unordered list with heapsort
        smallest() - O(n + k log n) retrieve the K highest priority elements

"""
class Heap():

    def __init__(self):
        self.heapArray = []
    
    def __str__(self):
        res = ""

        for i in range(len(self.heapArray)):
            lefChildIndex = self.getLeftChildIndex(i)
            rightChildIndex = self.getRightChildIndex(i)

            res += str(self.heapArray[i].value) + ": "

            if(lefChildIndex):
                res += str(self.heapArray[lefChildIndex].value)
            else:
                res += "(x)"

            res += " - "

            if(rightChildIndex):
                res += str(self.heapArray[rightChildIndex].value)
            else:
                res += "(x)"

            res += "\n"

        return res
    

    """
    getLeftChildIndex()

    - Returns the index of the left child

        Input:
        ------
            parentIndex : int
        
        Output:
        ------
            leftChidIndex : int
    """
    def getLeftChildIndex(self, parentIndex) -> int:
        index = (2*parentIndex)+1

        if(index >= len(self.heapArray)):
            return None
        else:
            return index

    """
    getRightChildIndex()

    - Returns the index of the right child

        Input:
        ------
            parentIndex : int
        
        Output:
        ------
            rightChidIndex : int
    """
    def getRightChildIndex(self, parentIndex) -> int:
        index = (2*parentIndex)+2

        if(index >= len(self.heapArray)):
            return None
        else:
            return index
    """
    getParentIndex()

    - Calculates the parent index based on the child index.

        Input:
        ------
            childIndex : int

        Output:
        -------
            parentIndex : int
    """
    def getParentIndex(self, childIndex) -> int:
        if childIndex % 2 == 0:        #Right child
            return int((childIndex-2)/2)
        elif (childIndex % 2 != 0):    #left child
            return int((childIndex-1)/2)
    

    """
    insert() - O(log n)

    - Insert a new node at the end of the tree and bubble it up to the correct position.

        Input:
        ------
            node : HeapNode

        Output:
        -------
            None
    """
    def insert(self, node: HeapNode) -> None:
            self.heapArray.append(node)                          #Add new node to the end of the tree
            childIndex = len(self.heapArray)-1                   #Get the new node's index (child)

            if childIndex != 0:                                  #If not the root
                isRightPosition = False                              #Flag indicating correct position for node found
                while(not isRightPosition and childIndex != 0):     #Look for the right position (or until reach the root)
                    parenIndex = self.getParentIndex(childIndex)       #Get parent index of the new node

                    if(self.heapArray[childIndex].value < self.heapArray[parenIndex].value):    #If child is smaller than its parent
                        temp = self.heapArray[parenIndex]                                       #Swap bubble fashion parent with children
                        self.heapArray[parenIndex] = self.heapArray[childIndex]
                        self.heapArray[childIndex] = temp

                        childIndex = parenIndex                 #CHildren will get (ex)parent's index for next iteration
                    else:       #If correct position
                        isRightPosition = True
            
    """
    swap()

    - To assist with the swapping of the nodes, avoidiing repetition of code. 
    - The function receives the index of the elements to be swapped

        Input:
        ------
            v1Index : int
            v2Index : int

        Output:
        ------
            None
    """
    def swap(self, v1Index, v2Index) -> None:
        temp = self.heapArray[v1Index]
        self.heapArray[v1Index] = self.heapArray[v2Index]
        self.heapArray[v2Index] = temp

    """
    remove() - O(log n)

    - Remove the element with the highest priority, adjusting the heap accordingly after removal.
    - The tree is adjusted by moving the last element of the heap to the root and then bubbling it down to the correct postition.

        Input:
        ------
            None
        
        Output:
        -------
            nodeRemoved : HeapNode
            None
    """
    def remove(self) -> HeapNode:

        if(len(self.heapArray) == 0):           #Heap is empty
            return None
        
        else:                                   #Heap is not empty
            #1) Remove root node
            nodeRemoved = self.heapArray.pop(0)     #Node being removed
            #2) Adjust the heap after removeal
            if(len(self.heapArray)  > 0):           #If heap not empty (Deal with Case 0)
                lastNode = self.heapArray.pop()     #Remove node from last position
                self.heapArray.insert(0,lastNode)     #Move last node to the root

                if(len(self.heapArray) > 1):        #If heap has more than one element (Deal with Case 1)
                    #(Case 3 - Bubble down)
                    parentIndex = 0                 #Node initial index before Bubble down
                    isRightPosition = False         #Flad indicating correct position has been found

                    while(not isRightPosition):
                        leftChildIndex = self.getLeftChildIndex(parentIndex)    #Get index of left child
                        rightChildIndex = self.getRightChildIndex(parentIndex)  #Get index of right child

                        if(leftChildIndex): #If there is a left child
                            if(rightChildIndex): #If there is a right child                 
                                #If parent is in the right position (smaller value than its children)
                                if(self.heapArray[parentIndex].value < self.heapArray[leftChildIndex].value and         
                                self.heapArray[parentIndex].value < self.heapArray[rightChildIndex].value):
                                    isRightPosition = True
                                else:
                                    #Compare which child is smaller                            
                                    if(self.heapArray[leftChildIndex].value <= self.heapArray[rightChildIndex].value):
                                        #Swap parent with left child
                                        self.swap(parentIndex, leftChildIndex)
                                        parentIndex = leftChildIndex                                   
                                    else:
                                        #Swap parent with right child
                                        self.swap(parentIndex, rightChildIndex) 
                                        parentIndex = rightChildIndex 
                            else:   #If there is no right child
                                #Compare which one is smaller (parent or left)
                                if(self.heapArray[leftChildIndex].value <= self.heapArray[parentIndex].value):
                                    #Swap parent with left child
                                    self.swap(parentIndex, leftChildIndex)
                                    parentIndex = leftChildIndex
                                else:
                                    isRightPosition = True         
                        else:
                            #Leaf node, correct position
                            isRightPosition = True

            return nodeRemoved
    
    """
    peek() - O(1)

    - Return the element with the highest priority

        Input:
        ------
            None
        
        Output:
        -------
            self.heapArray[0] : HeapNode
            None
    """
    def peek(self) -> HeapNode:
        if(len(self.heapArray) > 0):        #If heap not empty
            return self.heapArray[0]        #Returns element with highesst priority
        else:
            return None
    """
    heapSort() - O(n log n)

    - Perform the heapsort given a list.

        Input:
        ------
            unorderedList : list

        Output:
        -------
            orderedList : list
    """
    def heapSort(self,unorderedList : list)-> list:
        
        orderedList = []
        #Insert items in the heap
        for i in range(len(unorderedList)):
            newNode = HeapNode(unorderedList[i])
            self.insert(newNode)
        
        print(self)
        input()
        #Remove items from the heap
        for i in range(len(unorderedList)):
            orderedNode = self.remove()
            orderedList.append(orderedNode)
        
        return orderedList
    
    """
    smallest()  - O(n + k log n)

    - Return a list of the k highest priority items from the heap.

        Input:
        ------
            k : int
        Output:
        -------
            orderedValues : list
    """
    def  smallest(self, k: int=1) -> list:
        orderedValues = [] 
        
        for i in range(k):
            nodeRemoved = self.remove()
            if(nodeRemoved):
                orderedValues.append(nodeRemoved)
        


        return orderedValues

if __name__ == "__main__":
    h1 = HeapNode(5)
    h2 = HeapNode(7)
    h3 = HeapNode(30)
    h4 = HeapNode(1)
    h5 = HeapNode(2)
    h6 = HeapNode(0)

    heap = Heap()

    heap.insert(h1)
    heap.insert(h2)
    heap.insert(h3)
    heap.insert(h4)
    heap.insert(h5)
    heap.insert(h6)


    print(heap)

    nodeRemoved = heap.remove()
    nodeRemoved = heap.remove()
    nodeRemoved = heap.remove()

    print("Item removed: " + str(nodeRemoved.value))

    print(heap)

    aList = [54, 28, 79, 45, 6, 10, 86, 52, 14, 98, 90, 97, 67, 74, 2, 82, 64, 47, 41, 23, 75, 76, 9, 34, 95, 39, 68, 23, 83, 90]

    orderedList = Heap().heapSort(aList)

    for i in orderedList:
        print(i)   


    bHeap = Heap()
    bList = [4,7,44,8,5,3,89,0,4,23,857,23,76,34,568756,23,75,235,678]
    for i in bList:
        bHeap.insert(HeapNode(i))

    result = bHeap.smallest(5)

    for i in result:
     print(i, end=" ")