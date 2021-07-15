class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_map = {c: i for i, c in enumerate(order)}
        
        words = [[order_map[w] for w in word] for word in words]
        
        return all([w1<=w2 for w1,w2 in zip(words, words[1:])])
        
        

