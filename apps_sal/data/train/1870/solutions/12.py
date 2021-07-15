class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n=sum(count) 
        sm=0 
        curr=0
        mx=0 
        mode=-1
        minim=-1 
        maxim=-1
        mid1,mid2=-1,-1
        for i in range(256):
            curr+=count[i]
            sm+=(i*count[i]) 
            if mid1==-1 and curr>=n//2:
                mid1=i 
            if mid2==-1 and curr>=n//2+1:
                mid2=i 
            if count[i]>mx:
                mode=i 
                mx=count[i] 
            if minim==-1 and count[i]!=0:
                minim=i 
            if count[i]!=0:
                maxim=i 
        mean=sm/n 
        if n%2==0:
            median=(mid1+mid2)/2 
        else:
            median=mid1
        ans=[round(minim,5),round(maxim,5),round(mean,5),round(median,5),round(mode,5)]
        return ans 

