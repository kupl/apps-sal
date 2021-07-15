class Solution:
    def longestAwesome(self, s: str) -> int:
        mx = 0
        table = {frozenset(): -1}
        acs, cs = set(), set()
        for i,c in enumerate(s):
            acs.add(c)
            if c in cs: cs.remove(c)
            else: cs.add(c)
                
            fcs = frozenset(cs)
            if fcs in table:
                mx = max(mx,i-table[fcs])
            for c in acs:
                if c in cs:
                    cs.remove(c)
                    rfcs = frozenset(cs)
                    cs.add(c)
                    if rfcs in table:
                        mx = max(mx,i-table[rfcs])
                else:
                    cs.add(c)
                    rfcs = frozenset(cs)
                    cs.remove(c)
                    if rfcs in table:
                        mx = max(mx,i-table[rfcs])
            table[fcs] = min(table.get(fcs,float('inf')),i)
                
        return mx
        

