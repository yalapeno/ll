"Boran Sahindal lab 2 - troll. med LinkedQ Klass"

class Node:

    def __init__(self, x, next=None):
        self.data = x #Kan referera till värde av valfri typ
        self.next = next

class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        return "I AM JUST A LinkedQ OBJEKT"

    def enqueue(self,x):
        ny = Node(x)

        if self.first == None:# om kön är tom
            self.first = ny
            self.last = ny
            
        else:# om inte tom. 
            self.last.next = ny #sista nodens .next pekar den nya noden
            self.last = ny# och så blir den nya noden den sista 
            
            
    def dequeue(self):
        a = self.first.data
        self.first = self.first.next#nästförsta blir först
        return a

    def peek(self):
        if self.first != None:
            return self.first.data
        else:
            return None


    def isEmpty(self):
        if self.first:
            return False
        else:
            return True

        
"""q = LinkedQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
print(x,y)"""
