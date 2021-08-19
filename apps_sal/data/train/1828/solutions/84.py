class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        counter = collections.Counter(barcodes)

        pq = []

        for key, value in counter.items():
            heapq.heappush(pq, (-value, key))

        temp_list = []

        result = []

        while pq:

            k = 2

            while pq and k > 0:

                # print(pq)

                count, curr = heapq.heappop(pq)
                count = count * -1

                result.append(curr)

                if count > 1:
                    temp_list.append((count - 1, curr))

                k -= 1

            if len(temp_list) == 0 and len(pq) == 0:
                break

            while temp_list:

                count, curr = temp_list.pop()

                heapq.heappush(pq, (-count, curr))

        return result
