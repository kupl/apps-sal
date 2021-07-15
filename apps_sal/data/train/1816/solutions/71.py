# def within_hour(large,small):
#         if abs(large[0] - small[0]) >= 2:
#             return False
#         if large[0] - small[0] == 1 and small[1] < large[1]:
#             print(large,small)
#             return False
#         return True
# class Solution:
    
    
#     def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
#         sorted_list = sorted(zip(keyTime,keyName))
#         # print(sorted_list)
#         alerted = []
#         people = {}
#         for time_str,name in sorted_list:
#             if name not in alerted:
#                 time = [int(time_str[:2]),int(time_str[-2:])]
#                 if name in people.keys():
#                     if len(people[name]) == 2:
#                         if within_hour(time,people[name][1]):
#                             people[name].append(time)
#                             if not within_hour(time,people[name][0]):
#                                 del people[name][0]
#                             else:
#                                 alerted.append(name)
#                         else:
#                             people[name] = [time]
#                     else:
#                         if not within_hour(time,people[name][0]):
#                             people[name] = [time]
#                         else:
#                             people[name].append(time)
#                 else:
#                     people[name] = [time]
#         return sorted(alerted)
                        
class Solution:    
    def minutes(self,time):
        hr , m = time.split(\":\")
        return int(hr)*60 + int(m)
    
    def countOfCheckinsInOneHour(self,arr):
        if len(arr)<3 : return False
        maxx = 1
        arr = sorted(arr,key = lambda x: self.minutes(x))
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
        final = []
        for i in dictionary:
            if self.countOfCheckinsInOneHour(dictionary[i])[0]:
                final.append(i)
        return sorted(final)
