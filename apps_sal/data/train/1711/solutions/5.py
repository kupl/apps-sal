class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
      
    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])
      
    @classmethod
    def from_array(cls, arr):
        return cls(arr.pop(0), cls.from_array(arr)) if arr else None
    
    def filter(self, fn):
        return self.from_array([e for e in self.to_array() if fn(e)])
    
    def map(self, fn):
        return self.from_array(list(map(fn, self.to_array())))
