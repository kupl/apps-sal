class Solution:
    def peopleIndexes(self, com: List[List[str]]) -> List[int]:
        c = com[:]
        com.sort(key=lambda x: -len(x))
        index = 1
        while index < len(com):
            curr = set(com[index])
            if any(set(com[i]) & curr == curr for i in range(index)):
                com.pop(index)
            else:
                index += 1
        res = []
        for i in com:
            for j in range(len(c)):
                if i == c[j]:
                    res.append(j)
        return sorted(res)
