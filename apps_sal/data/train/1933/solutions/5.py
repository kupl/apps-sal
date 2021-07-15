class Solution:
     def complexNumberMultiply(self, a, b):
         indice1 = a.index('+')
         indice2 = b.index('+')
         real1 = int(a[0:indice1])
         unreal1 = int(a[indice1+1:-1])
         real2 = int(b[0:indice2])
         unreal2 = int(b[indice2+1:-1])
         return str(real1*real2-unreal1*unreal2)+'+'+str(unreal1*real2+real1*unreal2)+'i'

