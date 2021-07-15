class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
      
    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])
      
    @classmethod
    def from_array(cls, arr):
        c = None
        if len(arr) == 0: return c
        for i in range(len(arr)-1, -1, -1):
            c = Cons(arr[i], c)
        return c
    
    def filter(self, fn):
        buf = self
        t = []
        while buf is not None:
            if fn(buf.head):
                t.append(buf.head)
            buf = buf.tail
        return Cons.from_array(t)
    
    def map(self, fn):
        buf = self
        t = []
        while buf is not None:
            t.append(fn(buf.head))
            buf = buf.tail
        return Cons.from_array(t)
