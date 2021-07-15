PRIMES = {3,5,7,11,13,17}

class Node :
    def __init__(self,string) :
        self.next = None
        self.a = string
    def swap(self,i,j) :
        b = self.a[:i] + self.a[j] + self.a[i+1:j] + self.a[i] + self.a[j+1:]
        return Node(b)
start_node = Node('123456789')

class Queue :
    def __init__(self) :
        self.front = None
        self.back = None
    def enqueue(self,node) :
        if self.back is None :
            self.front = self.back = node
        else :
            self.back.next = node
            self.back = node
    def dequeue(self) :
        if self.front is None :
            return None
        else :
            node = self.front
            self.front = node.next
            if self.front is None :
                self.back = None
            return node
q = Queue()
q.enqueue(start_node)

di = {start_node.a:0}
def bfs(q,level) :
    if q.front is None :
        return
    q2 = Queue()
    while q.front is not None :
        n = q.dequeue()
        for i in range(8) :
            # check right
            if i%3<2 :
                if int(n.a[i])+int(n.a[i+1]) in PRIMES :
                    b = n.swap(i,i+1)
                    if b.a not in di :
                        di[b.a] = level+1
                        q2.enqueue(b)
            # check down
            if i<6 :
                if int(n.a[i])+int(n.a[i+3]) in PRIMES :
                    b = n.swap(i,i+3)
                    if b.a not in di :
                        di[b.a] = level+1
                        q2.enqueue(b)
    bfs(q2,level+1)

bfs(q,0)
for _ in range(int(input())):
    input()
    # n,k = map(int,input().split())
    # s = sorted(map(int,input().split()),reverse=True)
    clue = ''
    for i in range(3) :
        clue += ''.join(input().split())
    print(di.get(clue,-1))

