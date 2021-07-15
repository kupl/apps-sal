def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
        
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        arr = {}
        for i in range(len(deck)):
            if deck[i] in arr:
                arr[deck[i]] += 1
            else:
                arr[deck[i]] = 1
        list1 = list(arr.values())
        mi = list1[0]
        for c in list1[1::]:
            mi = gcd(mi , c)
        if mi < 2:
            return False
        for i in list(arr.values()):
            if i % mi != 0:
                return False
        return True

