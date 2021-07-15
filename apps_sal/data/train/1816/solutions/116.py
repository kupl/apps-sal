class Solution:
\tdef alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
\t\td = collections.defaultdict(list)
\t\tres = []
\t\tfor i in range(len(keyName)):
\t\t\ttime = int(keyTime[i][0:2]) * 60 + int(keyTime[i][3:])
\t\t\td[keyName[i]].append(time)
\t\tfor k, v in d.items():
\t\t\tv.sort()
\t\t\tfor i in range(len(v) - 2):
\t\t\t\tdiff = v[i + 2] - v[i]
\t\t\t\tif 0 < diff <= 60:
\t\t\t\t\tres.append(k)
\t\t\t\t\tbreak
\t\treturn sorted(res)















# from collections import defaultdict
# class Solution:
#     def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
#         dic = defaultdict(dict)
#         result = set()
#         l = len(keyName)
#         i = 0
#         while i < l:
#             if keyName[i] not in result:
#                 # print(keyTime[i][:2], \"old\")
#                 if keyTime[i][:2] not in dic[keyName[i]]:
#                     dic[keyName[i]][keyTime[i][:2]] = 1
#                 else:
#                     dic[keyName[i]][keyTime[i][:2]] += 1
#                 # print(dic, \"dic\")
#                 if dic[keyName[i]][keyTime[i][:2]] >= 3:
#                     result.add(keyName[i])
#                     i += 1
#                     continue
#                 if  keyTime[i][3:] == \"00\": 
#                     newKeyTime = str(int(keyTime[i][:2])-1)
#                     # print(newKeyTime, \"new\")
#                     if newKeyTime not in dic[keyName[i]]:
#                         dic[keyName[i]][newKeyTime] = 1
#                     else:
#                         dic[keyName[i]][newKeyTime] += 1
#                     if dic[keyName[i]][newKeyTime] >= 3:
#                         result.add(keyName[i])
#                         i += 1
#                         continue
#                 i += 1
#         return list(result)
        
