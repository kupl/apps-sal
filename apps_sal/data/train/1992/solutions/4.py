class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combs = []
        
        n = len(characters)
        # the order in self.combs is reverse lexicographical by going from bitmask of 0 upwards
        for bitmask in range((1<<n)): 
            if bin(bitmask).count('1') == combinationLength: 
                curr = []
                for j in range(n): 
                    if bitmask & (1 << n-j-1): 
                        curr.append(characters[j])
                self.combs.append(''.join(curr))


    def __next__(self) -> str:
        return self.combs.pop()

    def hasNext(self) -> bool:
        return self.combs


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

