class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        data = [i for i in range(1, m + 1)]
        hashMap = {}
        for i in range(1, m + 1):
            hashMap[i] = i - 1
        result = []
        for q in queries:
            position = hashMap[q]
            result.append(position)
            data = [data[position]] + data[0:position] + data[position + 1:]
            for (index, d) in enumerate(data):
                hashMap[d] = index

        return result
