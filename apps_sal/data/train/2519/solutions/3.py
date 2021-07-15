class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split()
        #print(len(arr))
        for i in range(len(arr)):
            #print(arr[i][:len(searchWord)])
            if arr[i][:len(searchWord)] == searchWord:
                return i+1
        return -1
