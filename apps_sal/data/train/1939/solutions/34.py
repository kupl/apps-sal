class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels= {'a', 'e', 'i', 'o', 'u'}
        output =[]
        bucket = [[] for _ in range(8)]
        signaturebucket = [{} for _ in range(8)]
        
        def makesignature(word):
            result =0
            index =0
            for char in word:
                num = ord(char)
                if num < 97: #uppdercase -> lower:
                    num = num + 32
                if num == ord('a') or num == ord('i') or num == ord('e') or num == ord('o') or num == ord('u'):
                    num =97 #originally 'a'              
                num =num -97
                result = result + 21**index * num
                index +=1
            return result
        for word in wordlist:
            bucket[len(word)].append(word)
        for i in range(len(bucket)):
            for word in bucket[i]:
                signature = makesignature(word)
                dic = signaturebucket[i]

                if signature in dic:                    
                    dic[signature].append(word)
                else:
                    dic[signature] = [word]

        candidate = []
        for query in queries:
            if len(query) > 7:
                output.append(\"\")
                continue
            querysignature = makesignature(query)
            if len(signaturebucket[len(query)]) > 0:
                if querysignature in signaturebucket[len(query)]:
                    candidate = signaturebucket[len(query)][querysignature]
            
            if len(candidate) ==0:
                output.append(\"\")
                continue
      
            result=[3,\"\"]
            for i, word in enumerate(candidate):

                total=-1
                for i in range(len(query)):
                    if query[i] == word[i]:
                        cur = 0
                    elif query[i].lower() == word[i].lower():
                        cur = 1
                    elif query[i].lower() in vowels and word[i].lower() in vowels:
                        cur = 2
                    else:
                        total = 3
                        break
                    if total == -1:
                        total = cur
                    elif total < cur:
                        total = cur
                if total < result[0]:
                    result = [total, word]
            output.append(result[1])
            print (result[1])
        return output
