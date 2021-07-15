from collections import Counter
 from math import ceil
 class Solution:
     def reorganizeString(self, S):
         """
         :type S: str
         :rtype: str
         """
         char_freq = Counter(S).most_common()
         max_freq = char_freq[0][-1]
         
         if max_freq > ceil(len(S)/2):
             return ''
         else:
             buckets = [[] for _ in range(max_freq)]
             print(char_freq)
             start = 0 
             for char,freq in char_freq:
                 print(char,freq)
                 for i in range(freq):
                     idx = (i+start)%max_freq
                     print(idx)
                     buckets[idx].append(char)
                 start+=freq
             
             return ''.join(''.join(bucket) for bucket in buckets)
         
         
