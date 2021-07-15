def reverseWords(str):
   str_split = str.split()
   rev_words = []
    
   for i in range(len(str_split)-1,-1,-1):
       rev_words.append(str_split[i])
    
   return ' '.join(rev_words)
