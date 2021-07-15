class Solution:
    
    def find_min_greater(self,a,x):
        start = 0
        end = len(a)-1
        while(start<end):
            mid = start+end
            mid = mid//2
            if(a[mid]<x and a[mid+1]>x):
                return mid+1
            elif(a[mid]<x):
                start = mid
            else:
                end = mid
        return start
    
    def avoidFlood(self, rains: List[int]) -> List[int]:
        last_rained = {}
        no_rain = []
        ans = []
        for i in range(len(rains)):
            if(rains[i]==0):
                no_rain.append(i)
                ans.append(1)
            else:
                lake = rains[i]
                ans.append(-1)
                if(lake not in last_rained.keys()):
                    last_rained[lake] = i
                else:
                    lr = last_rained[lake]
                    zl = len(no_rain)
                    if(len(no_rain)==0 or no_rain[zl-1]<lr):
                        return []
                    else:
                        empty = self.find_min_greater(no_rain,lr)
                        ans[no_rain[empty]] = lake
                        last_rained[lake]=i
                        no_rain.pop(empty)
        return ans
