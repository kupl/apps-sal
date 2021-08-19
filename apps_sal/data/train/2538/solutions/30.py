class Solution:

    def countLargestGroup(self, n: int) -> int:
        q = []
        for i in range(n - 10 + 1):
            q.append(i + 10)
        l = []
        for j in range(len(q)):
            p = 0
            for k in range(len(str(q[j]))):
                p = p + int(str(q[j])[k])
            l.append(p)
        q = Counter(l)
        x = 0
        print(q)
        for (j, i) in list(q.items()):
            if j < 10:
                q[j] = q[j] + 1
        print(q)
        for (j, i) in list(q.items()):
            if i == max(q.values()):
                x = x + 1
        if n < 10:
            return n
        else:
            return x
