class Solution:
     def topKFrequent(self, words, k):
         times_dict = {}
         for i in words:
             if i not in times_dict.keys():
                 times_dict[i] = 1
             else:
                 times_dict[i] += 1
         return_list = []
         for i in range(k):
             max = 0
             max_key = ""
             for j in times_dict.keys():
                 if times_dict[j] > max:
                     max = times_dict[j]
                     max_key = j
                 elif times_dict[j] == max and j < max_key:
                     max = times_dict[j]
                     max_key = j 
             del times_dict[max_key]
             return_list.append(max_key)
         return return_list
