class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        availables = [] # available days, will be sorted ascendingly 
        n = len(rains)
        ans = [-1]*n
        prev_rain = dict() # prev_rain[lake] tells us when it last rained on lake, assuming lake is full.
        
        for day in range(n):
            if rains[day] == 0:
                availables.append(day)
            else:
                lake = rains[day]
                if lake not in prev_rain:
                    prev_rain[lake] = day
                else:
                    # we must find the earliest available day to empty this lake
                    # after prev_rain[lake] then remove it from availables and 
                    # remove lake from prev_rain, and indicate this in the answer
                    if len(availables) == 0 or availables[-1] < prev_rain[lake]:
                        return []
                    low = 0
                    high = len(availables)-1
                    while low < high:
                        med = (low+high)//2
                        if availables[med] < prev_rain[lake]:
                            low = med+1
                        else:
                            high = med
                    chosen_day = availables[low]
                    availables.remove(chosen_day)
                    prev_rain[lake] = day
                    ans[chosen_day] = lake
        
        while availables:
            ans[availables[-1]] = 20
            availables.pop()
        
        return ans              
