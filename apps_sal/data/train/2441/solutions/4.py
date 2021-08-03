class Solution:
    def makeGood(self, s: str) -> str:
        listx = [('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('f', 'F'), ('g', 'G'), ('h', 'H'), ('i', 'I'), ('j', 'J'), ('k', 'K'), ('l', 'L'), ('m', 'M'), ('n', 'N'), ('o', 'O'), ('p', 'P'), ('q', 'Q'), ('r', 'R'), ('s', 'S'), ('t', 'T'), ('u', 'U'), ('v', 'V'), ('w', 'W'), ('x', 'X'), ('y', 'Y'), ('z', 'Z'), ('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'), ('E', 'e'), ('F', 'f'), ('G', 'g'), ('H', 'h'), ('I', 'i'), ('J', 'j'), ('K', 'k'), ('L', 'l'), ('M', 'm'), ('N', 'n'), ('O', 'o'), ('P', 'p'), ('Q', 'q'), ('R', 'r'), ('S', 's'), ('T', 't'), ('U', 'u'), ('V', 'v'), ('W', 'w'), ('X', 'x'), ('Y', 'y'), ('Z', 'z')]
        listy = [s[0]]
        empty = ''
        for i in range(1, len(s)):
            if listy:
                a = listy.pop()
                if (a, s[i]) not in listx:
                    listy.append(a)
                    listy.append(s[i])
            else:
                listy.append(s[i])
        if listy:
            return ''.join(listy)
        else:
            return empty
