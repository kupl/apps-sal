t = int(input())

class Container:
    def __init__(self):
        self.comp = [0, 0]
        self.state = -1
    def process(self):
        if self.state == -1 or self.state == 1:
            if self.comp == [1, 1]:
                self.state = 3
            else:
                self.state = 0
            self.comp[0] += 1
        elif self.state == 0 or self.state == 3:
            self.state = 1
            self.comp[1] += 1


for _ in range(t):
    n, k1, k2 = map(int, input().split())
    p1, p2, p3, p4 = map(int, input().split())
    containers = [Container() for _ in range(n)]
    sum = 0
    for i in range(1, n+1):
        con = [x for x in range(1, n+1) if x%i == 0]
        for ele in con:
            containers[ele-1].process()
    for ele in containers[k1-1:k2]:
        if ele.state == 0:
            sum += p2
        elif ele.state == 3:
            sum += p1
        elif ele.state == 1:
            sum+= p3
    print(sum)
