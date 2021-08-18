class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False

        counter = Counter(hand)

        nums = sorted(counter.keys())

        for num in nums:
            count = counter[num]
            if count == 0:
                continue
            min_count = count
            for i in range(W):
                if count[num + i] < min_count:
                    return False
                count[num + i] -= min_count
        return True

    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        if len(hand) % W != 0:
            return False

        counter = Counter(hand)
        q = []
        for num, freq in list(counter.items()):
            heapq.heappush(q, (num, freq))

        while q and len(q) >= W:
            tmp = []
            for i in range(W):
                x = heapq.heappop(q)
                if tmp and tmp[-1][0] + 1 != x[0]:
                    return False
                tmp.append(x)
            for num, freq in tmp:
                if freq > 1:
                    heapq.heappush(q, (num, freq - 1))
        return 0 == len(q)

    def isNStraightHand4(self, hand: List[int], W: int) -> bool:

        if len(hand) % W != 0:
            return False

        hand.sort()
        q = []
        for num in hand:
            if q and q[-1][0] == num:
                q[-1][1] += 1
            else:
                q.append([num, 1])

        n = len(hand)
        while n > 0:
            if len(q) < W:
                return False
            for i in range(1, W):
                if q[i][0] != q[i - 1][0] + 1:
                    return False
            j = 0
            for i in range(W):
                if q[j][1] == 1:
                    q.pop(j)
                else:
                    q[j][1] -= 1
                    j += 1
            n -= W
        return len(q) == 0

    def isNStraightHand3(self, hand: List[int], W: int) -> bool:
        counter = Counter(hand)
        while counter:
            m = min(counter)
            for k in range(m, m + W):
                v = counter[k]
                if not v:
                    return False
                if v == 1:
                    del counter[k]
                else:
                    counter[k] = v - 1
        return True
