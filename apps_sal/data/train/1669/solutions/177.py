class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        ogLen = len(hand)
        if W == 1:
            return True
        
        counter = Counter(hand)
        counted = [(key, counter[key]) for key in counter]
        counted.sort()
        
        print(counted)
        
        heapify(counted)
        
        groups = []
        
        
        
        
        group = []
        group.append(heappop(counted))
        
        tempStorage = set()
        
        while counted:
            
            n0 = group[-1]
            
            # print(n0[0], counted[0][0], group)
            
            if n0[0]+1 == counted[0][0]:
                n1 = heappop(counted)
                
            elif counted[0][0] > n0[0]+1:
                
                group = []
                group.append(heappop(counted))
                continue
            
            group.append(n1)
            
            if len(group) == W:
                # print(\"adding group\", group)
                groups.append(group)
                
                for val, count in group:
                    count -= 1
                    if count != 0:
                        heappush(counted, (val, count))
                
                # print(\"heap now: \", counted)
                group = []
                if counted:
                    group.append(heappop(counted))

        print((len(groups)*W, ogLen))
                
        return len(groups)*W == ogLen
            
            
            
            
            

