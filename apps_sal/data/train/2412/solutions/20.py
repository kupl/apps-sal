class Solution:
    def removeDuplicates(self, S: str) -> str:
        while True:
            counter = 0
            
            i = 1
            remove_list = []
            while i < len(S):
                if S[i] == S[i-1]:
                    counter = 1
                    remove_list.append(i)
                    i += 1
                i += 1
            for j in range(len(remove_list), 0, -1):
                idx = remove_list[j-1]
                if idx == len(S)-1:
                    S = S[:idx-1]
                else:
                    S = S[:idx-1] + S[idx+1:]
            if counter == 0: break
        return S
