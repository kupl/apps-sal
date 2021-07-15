class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # 1, 2, 2, 3, 3, 4, 6, 7, 8
        # 1 2 3
        #   2 3 4
        #         6 7 8
        
        # W length Q
        # how many opened
        # # of the element is current opened one
        
        q = deque()
        opened = 0
        last = 0
        counter = Counter(hand)
        for n in sorted(counter):
            count = counter[n]
            if n > last + 1 and opened > 0:
                return False
            
            if n == last + 1 and count < opened:
                return False
            
            
            q.append(count - opened)
            opened = count
            
            if len(q) == W:
                opened -= q.popleft()
            
            last = n
        return not opened
