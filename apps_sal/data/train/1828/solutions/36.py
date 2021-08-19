import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = {}
        for i in barcodes:
            if i not in count:
                count[i] = 0
            count[i] += 1

        heap = [(-v, k) for k, v in list(count.items())]
        heapq.heapify(heap)

        op = [None]
        i = 0

        while heap:
            temp = []
            while True:
                maxVal, maxKey = heapq.heappop(heap)
                if maxKey == op[-1]:
                    temp.append((maxVal, maxKey))
                else:
                    break

            op.append(maxKey)

            currVal = maxVal + 1
            if currVal < 0:
                heapq.heappush(heap, (currVal, maxKey))

            while temp:
                val, key = temp.pop()
                heapq.heappush(heap, (val, key))
            # print(\"This is heap:\",heap)
        return op[1:]
