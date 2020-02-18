
# Note: This Queue class is sub-optimal. Why?
class LinkedPair:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str({'data' : self.data, 'next' : self.next})

class LinkedList:
    def __init__(self,head=None):
        self.head = None if head == None else LinkedPair(head)
        self.tail = None if head == None else self.head
    
    def tails(self,val):
        if self.head == None:
            self.head = LinkedPair(val)
            self.tail = self.head
            return self.head
        else:
            self.tail.next = LinkedPair(val)
            self.tail = self.tail.next
            return self.tail
        # node = self.head
        # while node.next:
        #     node = node.next
        # node.next = LinkedPair(val)
        # self.tail = node
    
    def heads(self,val):
        new_head = LinkedPair(val)
        new_head.next = self.head
        self.head = new_head
    
    def remove_head(self):
        self.head = self.head.next
    
    def __repr__(self):
        linked_list = []
        node = self.head
        while node:
            linked_list.append(node.data)
            node = node.next
        return str(linked_list)

class Queue():
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value):
        self.queue.tails(value)

    def dequeue(self):
        if self.size > 0:
            return self.queue.remove_head()
        else:
            return None
    @property
    def size(self):
        size = 0
        node = self.queue.head
        while node:
            size += 1
            node = node.next
        return size
    
    def __repr__(self):
        return str(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size > 0:
            return self.stack.pop()
        else:
            return None
    @property
    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    ll = LinkedList(20)
    ll.tails(21)
    ll.tails(22)
    ll.tails(23)
    ll.heads(17)
    ll.heads(13)
    print(ll)

    q = Queue()
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(50)
    q.dequeue()
    q.enqueue(11)
    q.enqueue(16)
    q.dequeue()

    print(q)
