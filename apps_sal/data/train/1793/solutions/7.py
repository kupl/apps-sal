from math import factorial

class PlayingCards:    
    
    def __init__(self):
        
        self.chars = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        self.ranks = 'A23456789TJQK'
        self.suits = 'CDHS'
        self.cards = [rank + suit for suit in self.suits for rank in self.ranks]

    def encode(self, message):

        if any(ch not in self.chars for ch in message):
            return None
        
        char_vals = {v: i for i, v in enumerate(self.chars)}
        perm_ind = sum(int(self.n_to_base_27(char_vals[ch])*27**(len(message) - i - 1)) for i, ch in enumerate(message))
        
        if perm_ind >= factorial(52):
            return None
        
        return self.card_permutation(perm_ind)
    
    def decode(self, deck):
      
        if not all(card in self.cards for card in deck) or len(set(deck)) != 52:
            return None
        
        val_chars = {i: v for i, v in enumerate(self.chars)}
        lex_index = 0

        for i in range(len(deck)):
            s = 0
            for j, v in enumerate(deck[i + 1:]):
                if self.cards.index(v) < self.cards.index(deck[i]):
                    s += 1 
            lex_index += s*factorial(len(deck) - i - 1) 
            
        char_arr = []
        while lex_index:
            lex_index, i = divmod(lex_index, 27)
            char_arr.append(val_chars[i])
            
        return ''.join(char_arr[::-1])
    
    @staticmethod
    def n_to_base_27(n):
        
        if n == 0:
            return 0
        d = []
        while n:
            d.append(n%27)
            n //= 27
        return int(''.join(map(str, d[::-1])))

    def card_permutation(self, k):
        
        factorial_arr = [1]
        for i in range(2, 52):
            factorial_arr.append(factorial_arr[-1] * i)

        permutation = []
        res = list(range(52))

        while factorial_arr:
            factorial = factorial_arr.pop()
            n, k = divmod(k, factorial)
            permutation.append(res[n])
            res.remove(res[n])
        permutation.append(res[0])

        return [self.cards[i] for i in permutation]
