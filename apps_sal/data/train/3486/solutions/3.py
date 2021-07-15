class Cycle:
    def __init__(self, n):
        self.length = n
        self.h = current = node = Node(1)
        for i in range(2, n+1):
            current.next = Node(i)
            current = current.next
        current.next = node
        
    def minimize(self, n):
        current = Node(0)
        current.next = self.h
        while self.length > 1:
            for i in range((n - 1) % self.length):
                current = current.next
            current.next = current.next.next
            self.length -= 1
            pass
        return current.next.n
    
class Node:
    def __init__(self, n):
        self.n = n
        self.next = None
    
def find_last(n, m):
    x = n - m
    return (Cycle(n).minimize(m), (1 + x) * x + (n - 1) * m)
