class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        count = {}
        limit = (len(S) + 1) / 2
        for c in S:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

            if (count[c] > limit):
                return("")

        pq = []
        for x in count.keys():
            c = count[x]
            pq.append((-c, x))

        heapq.heapify(pq)

        result = []
        while len(pq) >= 2:
            count1, char1 = heapq.heappop(pq)
            count2, char2 = heapq.heappop(pq)
            result.extend([char1, char2])

            if (count1 != -1):
                heapq.heappush(pq, (count1 + 1, char1))
            if (count2 != -1):
                heapq.heappush(pq, (count2 + 1, char2))

        answer = "".join(result)
        if (len(pq) == 1):
            answer += heapq.heappop(pq)[1]

        return(answer)
