class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips=sorted(trips, key=lambda x:x[1])
        cap=capacity
        st=[]
        for trip in trips:
            if not st:
                if cap<trip[0]:
                    return False
                st.append((trip[0], trip[-1]))
                cap-=trip[0]
            else:
                st=sorted(st, key=lambda x:x[1])
                while st and trip[1]>=st[0][1]:
                    cap+=st[0][0]
                    st.pop(0)
                if cap<trip[0]:
                    return False
                st.append((trip[0], trip[-1]))
                cap-=trip[0]
        return True
                
                    

