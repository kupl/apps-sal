class Solution:
  def longestAwesome(self, s: str) -> int:
    
    first_pos = [ -1 for i in range(1024) ]
    first_pos[0] = 0

    cur_xor = 0
    xors = [0] + [1<<i for i in range(10)]
    
    max_len = 0
    for i in range(len(s)):
      cur_xor = cur_xor ^ (1<<int(s[i]))
#      print(i, s[i], bin(cur_xor), end=\" \")
      for try_xor in xors:
#        print(try_xor, end = \" \")
        prev_xor = cur_xor ^ try_xor
        if first_pos[prev_xor] != -1:
#          print(bin(prev_xor), first_pos[prev_xor], end=\"|\")
          max_len = max(max_len, i - first_pos[prev_xor] + 1)
      
      if first_pos[cur_xor] == -1:
        first_pos[cur_xor] = i+1
        
      
    return max_len
