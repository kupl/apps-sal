class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_string = ''
        for s in address:
            if s == '.':
                new_string += '[.]'
            else:
                new_string += s
        return new_string
