class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        pos_detail = []
        complete_cell = [False] * len(target)
        check_next = []
        steps = []
        for i in range(len(target) - len(stamp) + 1):
            match = set()
            unmatch = set()
            for j in range(len(stamp)):
                if target[i + j] == stamp[j]:
                    match.add(i + j)
                else:
                    unmatch.add(i + j)
            pos_detail.append((match, unmatch))
            if not unmatch:
                steps.append(i)
                for j in range(max(0, i - len(stamp) + 1),
                               min(len(target) - len(stamp) + 1, i + len(stamp))):
                    check_next.insert(0, j)
                for j in range(len(stamp)):
                    complete_cell[i + j] = True
        while check_next:
            i = check_next.pop(0)
            match, unmatch = pos_detail[i]
            if not unmatch:
                continue
            for j in range(len(stamp)):
                if i + j in unmatch and complete_cell[i + j]:
                    unmatch.remove(i + j)
            if not unmatch and match:
                steps.insert(0, i)
                for j in range(len(stamp)):
                    complete_cell[i + j] = True
                for j in range(max(0, i - len(stamp) + 1),
                               min(len(target) - len(stamp) + 1, i + len(stamp))):
                    check_next.append(j)
        return steps if all(complete_cell) else []
