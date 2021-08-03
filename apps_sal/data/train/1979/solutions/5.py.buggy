class Solution:

    def largestTimeFromDigits(self, arr: List[int]) -> str:
        all_zero = True
        for item in arr:
            if item != 0:
                all_zero = False
        
        if all_zero:
            return \"00:00\"
        if min(arr) >= 3:
            return \"\"
        
        time = [0,0]
        

        def is_valid_hour(hour: int)->bool:
            return 0 <= hour and hour <= 23

        def is_valid_minute(minute: int)->bool:
            return 0 <= minute and minute <= 59

        def compare_and_update(time2: list)->None:
            if time2[0] > time[0]:
                time[0] = time2[0]
                time[1] = time2[1]
            elif time2[0] == time[0]:
                if time2[1] > time[1]:
                    time[1] = time2[1]
            else:
                pass

        for i in arr:
            sub1 = arr.copy()
            sub1.remove(i)
            for j in sub1:
                hr = i*10 + j
                if is_valid_hour(hr):
                    sub2 = sub1.copy()
                    sub2.remove(j)
                    mn1 = sub2[0]*10 + sub2[1]
                    mn2 = sub2[1]*10 + sub2[0]
                    if is_valid_minute(mn1):
                        new_time = [hr,mn1]
                        compare_and_update(new_time)
                    if is_valid_minute(mn2):
                        new_time = [hr,mn2]
                        compare_and_update(new_time)


        h2 = time[0] % 10 ; time[0] //= 10
        h1 = time[0]

        m2 = time[1] % 10 ; time[1] //= 10
        m1 = time[1]
        
        if h1 == h2 and h2 == m1 and m1 == m2 and m2 == 0:
            return \"\"

        return f\"{h1}{h2}:{m1}{m2}\"
        
