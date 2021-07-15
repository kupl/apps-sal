import itertools

from abc import ABC, abstractmethod

class Syntax(ABC):
    def __init__(self, next=None):
        self.next = next
    
    @abstractmethod
    def get_values(self):
        return []
    
    def get_strings(self):
        if self.next is None:
            return self.get_values()
        
        return (a+b for a in self.get_values() for b in self.next.get_strings())
    
class Letter(Syntax):
    def __init__(self, letter, next=None):
        super().__init__(next)
        self.letter = letter
        
    def get_values(self):
        return [self.letter]
    
class Union(Syntax):
    def __init__(self, elts, next=None):
        super().__init__(next)
        self.elts = elts
        
    def get_values(self):
        return itertools.chain(*[elt.get_strings() for elt in self.elts])
    
class Solution:
    def find_close_brace(self, expression, offset):
        level = 1
        
        while level:
            offset += 1
            if expression[offset] == '{':
                level += 1
            elif expression[offset] == '}':
                level -= 1
        
        return offset
    
    def split_union_commas(self, expression):
        left = 0
        curr = 0
        
        expressions = []
        
        while left < len(expression):
            if expression[curr] == '{':
                curr = self.find_close_brace(expression, curr) + 1
            elif expression[curr] == ',':
                expressions.append(expression[left:curr])
                curr += 1
                left = curr
            else:
                curr += 1
                
            if curr == len(expression):
                expressions.append(expression[left:curr])
                break
                
        return expressions
    
    def parse(self, expression, offset):
        if offset == len(expression):
            return None
        
        if expression[offset] != '{':
            # this is a letter
            try:
                word_end = expression.index('{', offset)
            except ValueError:
                word_end = len(expression)
                
            return Letter(expression[offset:word_end], self.parse(expression, word_end))
        
        # parse union
        close_idx = self.find_close_brace(expression, offset)
        return Union(self.parse_union(expression[offset+1:close_idx]), self.parse(expression, close_idx+1))
        
    def parse_union(self, expression):
        elts = self.split_union_commas(expression)
        return [self.parse(elt, 0) for elt in elts]
    
    def braceExpansionII(self, expression: str) -> List[str]:
        head = self.parse(expression, 0)
        if head is None:
            return []
        
        return sorted(list(set(head.get_strings())))
