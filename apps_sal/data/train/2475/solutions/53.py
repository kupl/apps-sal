class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        prev = A[0]
        indices = {i for i in range(len(prev))}
        remove = set()
        for a in A[1:]:
            remove.clear()
            for i in indices:
                if prev[i] > a[i]:
                    remove.add(i)
            indices -= remove
            prev = a
        return len(prev) - len(indices)
