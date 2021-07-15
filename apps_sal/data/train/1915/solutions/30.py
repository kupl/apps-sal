class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        done = [False]*n
        from collections import deque
        ans = []
        queue = deque()
        A = []
        for i in range(n-m+1):
            todo, made = set(), set()
            for j, ch in enumerate(stamp):
                a = target[i+j]
                if a == ch:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))
            if not todo:
                ans.append(i)
                for k in made:
                    if not done[k]:
                        done[k] = True
                        queue.append(k)
        
        while queue:
            i = queue.popleft()
            for j in range(max(0, i-m+1), min(i, n-m)+1):
                if i in A[j][1]:
                    A[j][1].discard(i)
                    if not A[j][1]:
                        ans.append(j)
                        for k in A[j][0]:
                            if not done[k]:
                                done[k] = True
                                queue.append(k)
        return ans[::-1] if all(done) else []

