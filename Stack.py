import LinkedList as ll
class Stack:
    """Class representing a stack (LIFO) implemented using a linked list."""
    
    def __init__(self):
        """Initializes an empty stack."""
        self.lst = ll.LinkedList()
    
    def is_empty(self):
        """Returns True if the stack is empty, otherwise False."""
        return self.lst.is_empty()
    
    def __len__(self):
        """Returns the number of elements in the stack."""
        counter = 0
        actNode = self.lst.head
        while actNode != self.lst.endnode:
            counter += 1
            actNode = actNode.next
        return counter
    
    def push(self, data):
        """Adds an element to the top of the stack."""
        self.lst.insert_at_beginning(data)
    
    def pop(self):
        """Removes the top element of the stack and returns data from it.
        Raises an error if the stack is empty.
        """
        if self.lst.is_empty():
            raise Exception('Stack is empty')
        return self.lst.remove_first()
    
    def top(self):
        """Returns data from the top element of the stack without removing it.
        Raises an error if the stack is empty.
        """
        if self.lst.is_empty():
            raise Exception('Stack is empty')
        return self.lst.head.data

class Queue:
    """Class representing a queue (FIFO) implemented using a linked list."""
    
    def __init__(self):
        """Initializes an empty queue."""
        self.lst = ll.LinkedList()
        self.length = 0
    
    def is_empty(self):
        """Returns True if the queue is empty, otherwise False."""
        return self.lst.is_empty()
    
    def __len__(self):
        """Returns the number of elements in the queue."""
        return self.length
    
    def enqueue(self, data): 
        """Adds an element to the end of the queue."""
        self.lst.append(data)
        self.length += 1
    
    def dequeue(self):
        """Removes the front element of the queue and returns data from it.
        Raises an error if the queue is empty.
        """
        if self.lst.is_empty():
            raise Exception('Queue is empty')
        self.length -= 1
        return self.lst.remove_first()
    
    def front(self):
        """Returns data from the front element of the queue without removing it.
        Raises an error if the queue is empty.
        """
        if self.lst.is_empty():
            raise Exception('Queue is empty')
        return self.lst[0]




def test_stack():
    s = Stack()
    
    print("start:", len(s), s.is_empty())

    for x in range(10):
        s.push(x)
    
    print("after push:", len(s), s.is_empty())
    
    while not s.is_empty():
        print(s.top(), s.pop())

    print("end:", len(s), s.is_empty())

def test_queue():
    q = Queue()
    print("start:", len(q), q.is_empty())
    for i in range(10):
        q.enqueue(i)
    print("after push",q.front(), q.is_empty(), len(q))
    q.enqueue(12)
    print("print after added data:", q.front(), q.is_empty())
    q.dequeue()
    print("after removed data", q.front())
    print(f"first element: {q.front()}")

    while not q.is_empty():
        print(q.front(), q.dequeue())
    print("after removing data:", q.is_empty())

if __name__ == "__main__":
    test_stack()
    #test_queue()
