class Solution:
    def timeDifference(self,A,B):
        A_hr ,A_min = A.split(\":\")
        B_hr ,B_min = A.split(\":\")
        A_time = int(A_hr)*60 + int(A_min)
        B_time = int(B_hr)*60 + int(B_min)
        return B_time-A_time
    
    def minutes(self,time):
        hr , m = time.split(\":\")
        return int(hr)*60 + int(m)
    
    def countOfCheckinsInOneHour(self,arr):
        if len(arr)<3 : return False
        maxx = 1
        arr = sorted(arr,key = lambda x: self.minutes(x))
        print(arr)
        counter = 1
        for j in range(len(arr)):
            counter = 1
            start = j
            for i in range(j+1,len(arr)):
                if 0< self.minutes(arr[i]) - self.minutes(arr[start]) <= 60:
                    counter += 1
                    maxx = max(maxx,counter)
                elif self.minutes(arr[i]) - self.minutes(arr[start]) >60 or self.minutes(arr[i]) - self.minutes(arr[start]) <0:
                    maxx = max(maxx,counter)
                    counter = 1
                    start = i
        if maxx >= 3 : return True,maxx
        return False,maxx
    
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dictionary = {}
        for name,time in zip(keyName,keyTime):
            if name not in dictionary : dictionary[name] = [] 
            dictionary[name].append(time)
        print(dictionary)
        final = []
        for i in dictionary:
            if self.countOfCheckinsInOneHour(dictionary[i])[0]:
                final.append(i)
        return sorted(final)
