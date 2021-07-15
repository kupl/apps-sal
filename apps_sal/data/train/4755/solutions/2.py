class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binn = bin(N)
        binn = binn[2:]
        binn = binn.replace('0','#')
        binn = binn.replace('1','0')
        binn = binn.replace('#','1')
        return int(binn,2)
