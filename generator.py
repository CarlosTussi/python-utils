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

    def getNext(self):
        current = self.firstLink
        while(current):
            yield current
            current = current.next


linkedlist = LinkedList()


alist = [4,6,33,7,8,2,79,3,9]
for i in alist:
    linkedlist.addElement(Link(i))

gen = linkedlist.getNext()
print(gen.__next__())

for i in gen:
    print(i)