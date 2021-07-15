import heapq
class HeapDict:
    def __init__(self):
        self.h = []
        self.d = {}

    def insert(self,x):
        if x not in self.d or self.d[x] == 0:
            heapq.heappush(self.h, x)
        self.d.setdefault(x,0)
        self.d[x] += 1


    def erase(self,x):
        if x not in self.d or self.d[x] == 0:
            return
        else:
            self.d[x] -= 1

        while self.h:
            if self.d[self.h[0]] == 0:
                heapq.heappop(self.h)
            else:
                break


    def get_min(self):
        if not self.h:
            return None
        else:
            return self.h[0]


    def pop(self):
        poped_val = self.h[0]
        self.erase(poped_val)
        return poped_val


    def exist(self, x):
        return (x in self.d and self.d[x] > 0)


    def show_h(self):
        elems = [v for v in self.h if self.d[v] > 0]
        print(elems)


    def show_d(self):
        print(self.d)



def main():
    n,q = map(int, input().split())
    eventl = []

    for _ in range(n):
        s,t,x = map(int, input().split())
        eventl.append((s-x, 'a-stop', x)) 
        eventl.append((t-x, 'b-start', x))

    for i in range(q):
        d = int(input())
        eventl.append((d,'c-go', i))

    eventl.sort()

    ans = [0]*q
    hd = HeapDict()
    for e in eventl:
        if e[1] == 'a-stop':
            hd.insert(e[2])
        elif e[1] == 'b-start':
            hd.erase(e[2])
        else:
            min_x = hd.get_min()
            if min_x is not None:
                ans[e[2]] = min_x
            else:
                ans[e[2]] = -1

    for a in ans:
        print(a)


def __starting_point():
    main()
__starting_point()
