class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hmap = {}
        for h in hand : 
            if h not in hmap : hmap[h] = 0
            hmap[h] +=1
        
        cards = sorted(list(hmap.keys()))
        #print(hmap,cards)
        
        for card in cards :
            #print(hmap)
            while card in hmap :
                for n in range(card,card+W) :
                    if n not in hmap : 
                        #print(hmap,\"pop\",n,card)
                        return False
                    else : 
                        hmap[n] -=1
                        if hmap[n] == 0 : 
                            
                            del(hmap[n])
                            #print(hmap,\"pop\",n,card)
        #print(hmap,\"k\")
        if hmap : return False 
        return True
