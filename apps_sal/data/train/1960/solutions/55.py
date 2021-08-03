class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        array = []

        element2index = {}
        index2element = {}

        for i in range(m):
            element2index[i + 1] = i
            index2element[i] = i + 1

        for i in range(len(queries)):

            q = queries[i]

            pos = element2index[q]

            array.append(pos)

            for k in range(pos - 1, -1, -1):

                e = index2element[k]
                element2index[e] += 1
                index2element[element2index[e]] = e

            index2element[0] = q
            element2index[q] = 0

        return array
