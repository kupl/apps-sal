class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cell = 0
        for c in cells:
            cell = (cell << 1) | c
        seendict = {}
        index = 0
        while True:
            # print([int(x) for x in '{0:08b}'.format(cell)])
            if cell in seendict:
                if (N - index) % (index - seendict[cell]) == 0:
                    return [int(x) for x in '{0:08b}'.format(cell)]
            seendict[cell] = index
            not_cell = (cell ^ 255) 
            cell = ((cell << 1) & (cell >> 1)) | ((not_cell << 1) & (not_cell >> 1))
            index += 1
