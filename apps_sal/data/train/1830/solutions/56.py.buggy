def nex(arr, target): 
\tstart = 0;
\tend = len(arr) - 1

\tans = -1; 
\twhile (start <= end): 
\t\tmid = (start + end) // 2; 

\t\t# Move to right side if target is 
\t\t# greater. 
\t\tif (arr[mid] <= target): 
\t\t\tstart = mid + 1; 

\t\t# Move left side. 
\t\telse: 
\t\t\tans = mid; 
\t\t\tend = mid - 1; 

\treturn ans;
            
def find(ind,dind,flag):
    n=len(dind)
    if n==0:
        flag[0]=1
        return -1
    ans = nex(dind,ind)
    if ans==-1:
        flag[0]=1
        return ans
    else:
        return dind[ans]
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lind={}
        n = len(rains)
        ans = [1 for i in range(n)]
        dind = []
        for i in range(n):
            if rains[i] >0:
                ans[i]=-1
                if rains[i] not in lind:
                    lind[rains[i]]=i
                    
                else:
                    flag=[0]
                    ind = lind[rains[i]]
                    dry = find(ind,dind,flag)
                    if flag[0]==1:
                        return []
                    else:
                        ans[dry] = rains[i]
                        lind[rains[i]]=i
                        dind.remove(dry)
            else:
                dind.append(i)
                
        return ans
            
