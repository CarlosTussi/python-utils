class Link():

    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.key)


class LinkedList():
    
    def __init__(self, firstLink : Link = None):
        self.firstLink = firstLink
    
    def __str__(self):
        pass

    def __iter__(self):
        self.current = self.firstLink       #Define the attribute to contain the value of each iteration
        return self


    def __next__(self):
        currentElement = self.current       #Declare currentElement to be returned
        if(self.current):                   #Update the iterator attribute with the value for the next iteration
            self.current = self.current.next
            return currentElement
        else:
            raise StopIteration
        

    def addElement(self, element):
        current = self.firstLink          

        if(current):
            previous = None
            while(current):
                previous = current
                current = current.next
            previous.next = element
        else:
            self.firstLink = element
    
    def traverse(self):
        current = self.firstLink
        while(current):
            print(current, end=" ")
            current = current.next


linkedlist = LinkedList()


alist = [4,6,33,7,8,2,79,3,9]

for i in alist:
    linkedlist.addElement(Link(i))

linkedlist.traverse()

blist = [9,8,7,6,5,4,3,2,1,0]

linkedList2 = LinkedList()
for i in blist:
    linkedList2.addElement(Link(i))

iterator = iter(linkedList2)

for elem in iterator:
    print(elem, end=" ")