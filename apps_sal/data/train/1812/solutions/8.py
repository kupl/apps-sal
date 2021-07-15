    
from math import log2

class Node:
    def __init__(self,val,freq):
        self.val=val
        self.freq = freq
        
class MajorityChecker:

    def __init__(self, arr: List[int]):
        
        self.arr = arr
        self.locations = {}
        for i,val in enumerate(arr):
            if val in self.locations:
                self.locations[val].append(i)
            else:
                self.locations[val] = [i]
        self.occur = sorted(list(self.locations.items()), reverse=True, key=lambda x: len(x[1]))
    
        print((self.occur))
        
#         self.freq = { i:[] for i in arr }
        
#         self.size = 1 << math.ceil(log2(len(arr))) + 1
        
#         self.st = [0]*self.size
        
#         self.build(0,len(arr)-1,0)
    
        
    
#     def merge(self,a,b):
#         if a.val == b.val:
#             return Node(a.val, a.freq + b.freq)
#         if a.freq>b.freq:
#             return Node(a.val, a.freq-b.freq)
#         return Node(b.val,b.freq-a.freq)
    
#     def pqery(self,l,r,pos,s,e):
#         if s>r or e<l:
#             return Node(0,0)
        
#         if l<=s and r>=e:
#             return self.st[pos]
        
#         mid  = ( s + e )>>1
        
#         a=self.pqery(l,r,2*pos + 1,s,mid)
#         b=self.pqery(l,r,2*pos + 2,mid+1,e)
#         return self.merge(a,b)
        
#     def build(self,start,end,pos):
        
#         if start==end:
#             self.st[pos]=Node(self.arr[start],1)
#             self.freq[self.arr[start]].append(start)
        
#         else:
            
#             mid = (end + start)>>1

#             self.build(start,mid,2*pos + 1)
#             self.build(mid+1,end,2*pos + 2)
#             self.st[pos] = self.merge(self.st[pos*2 + 1],self.st[2*pos + 2])
            
            
    def lower_bound(self,arr,x):
        l=0
        r=len(arr)-1
        while l<=r:
            mid = (l+r )>> 1
            if arr[mid]<x:
                l=mid+1
            else:
                r=mid-1
        return l
            
            
    def upper_bound(self,arr,x):
        l=0
        r=len(arr)-1
        while l<=r:
            mid = (l+r) >> 1
            if arr[mid]<=x:
                l=mid+1
            else:
                r=mid-1
        return r+1
            
        
    def query(self, left: int, right: int, threshold: int) -> int:
        for i,j in self.occur:
            if len(j)<threshold:
                return -1
            s = self.lower_bound(j,left)
            e = self.upper_bound(j,right)
            if e-s>=threshold:
                return i
            
        return -1
#         candidate = self.pqery(left,right,0,0,(len(self.arr)-1))
#         # print(self.freq,candidate.val)
#         if candidate.val==0:return -1
        
#         s = self.lower_bound(self.freq[candidate.val],left)
#         e= self.upper_bound(self.freq[candidate.val],right)
#         # print(e,s)
#         if (e-s) >=threshold :
#             return candidate.val
#         else:
#             return -1


        


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

