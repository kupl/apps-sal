class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        hashmap = defaultdict(int)
        for i in B:
            c = defaultdict(int)
            for p in i:
                c[p] += 1
            for n in c:
                hashmap[n] = max(hashmap[n], c[n])
        result = []
        for i in A:
            count = defaultdict(int)
            for c in i:
                count[c] += 1
            flag = True
            for node in hashmap:
                if node not in count or count[node] < hashmap[node]:
                    flag = False
            if flag:
                result.append(i)
        return result
