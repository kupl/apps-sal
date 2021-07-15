class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        from math import floor, log
        def pos2num(row, pos):
            if row %2 == 0:
                return 2**row + pos
            else:
                return 2**(row+1) - pos - 1
        targetrow = floor(log(label)/log(2))
        if targetrow %2 == 0:
            targetpos = label - 2**targetrow
        else:
            targetpos = 2**(targetrow+1) - label -1
        row = 0
        out = []
        offset = 0
        posoffset = 0
        while row <= targetrow:
            out.append(pos2num(row, posoffset))
            posoffset *=2
            if targetpos < offset + 2**(targetrow - row - 1):
                #go left
                pass
            else:
                #go right
                offset += 2**(targetrow - row - 1)
                posoffset +=1
            #out.append(pos2num(row, offset))
            row +=1
        return out

