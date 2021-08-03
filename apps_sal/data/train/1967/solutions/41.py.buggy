class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        unvisited = []
        for i1 in range(1, len(S)):
            s1 = S[:i1]
            if s1 != \"0\" and s1.startswith(\"0\"):
                continue
            for i2 in range(i1 + 1, len(S)):
                s2 = S[i1:i2]
                if s2 != \"0\" and s2.startswith(\"0\"):
                    continue
                unvisited.append(([int(s1), int(s2)], i2))
        
        while unvisited:
            sequence, suffix_i = unvisited.pop()

            if suffix_i == len(S):
                return sequence

            next_term = sequence[-2] + sequence[-1]

            if next_term <= (1 << 31) - 1:
                next_term_s = str(next_term)
                new_suffix_i = suffix_i + len(next_term_s)
                if S[suffix_i:new_suffix_i] == next_term_s:
                    unvisited.append((sequence + [next_term], new_suffix_i))

