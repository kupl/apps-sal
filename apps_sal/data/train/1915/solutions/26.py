class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        from collections import deque
        m, n = len(stamp), len(target)
        queue = deque()
        done = [False]*n
        ans = []
        A = []
        for i in range(n-m+1):
            todo, made = set(), set()
            for j in range(m):
                if stamp[j] == target[i+j]:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((todo, made))
            if not todo:
                ans.append(i)
                for j in made:
                    if not done[j]:
                        done[j] = True
                        queue.append(j)
        while queue:
            i = queue.popleft()
            for j in range(max(0, i-m+1), min(i, n-m)+1):
                if i in A[j][0]:
                    A[j][0].discard(i)
                    if not A[j][0]:
                        ans.append(j)
                        for k in A[j][1]:
                            if not done[k]:
                                done[k] = True
                                queue.append(k)
                                
        return ans[::-1] if all(done) else []

