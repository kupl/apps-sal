class Solution:
    def countCharacters(self, words, chars: str) -> int:
        myd = {}
        for i in chars:
            if hash(i) in list(myd.keys()):
                myd[hash(i)] +=1
            else:
                myd[hash(i)]= 1
        wdata = []
        for i in range(0,len(words)):
            x = dict()
            for letter in words[i]:
                if hash(letter) in list(x.keys()):
                    x[hash(letter)]+=1
                else:
                    x[hash(letter)]=1
            wdata.append(x)
        count = 0
        for data in wdata:
            allin = True
            lcount = 0
            for letter in list(data.keys()):
                if letter in list(myd.keys()):
                    if data[letter] > myd[letter]:
                        allin = False
                    else:
                        lcount+=data[letter]
                else:
                    allin = False
            if allin == True:
                count+= lcount
        return count
        
        
#     def countCharacters(self, words: List[str], chars: str) -> int:
#         myd = {}
#         count = 0
#         for i in chars:
#             if i in myd.keys():
#                 myd[i] +=1
#             else:
#                 myd[i]= 1
        
#         for word in words:
#             allin = True

#             for letter in word:
#                 if letter in myd.keys():
#                     if word.count(letter) > myd[letter]:
#                         allin = False
#                 else:
#                     allin = False
#             if allin==True:
#                 count+=len(word)
#         return count

