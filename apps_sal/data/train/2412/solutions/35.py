class Solution:
    def removeDuplicates(self, S: str) -> str:
        if S.count(S[0]) == len(S):
            if len(S) % 2 == 0:
                return ''
            else:
                return S[0]
        while True:
            Sbuffer = S[0]
            new_string = S[0]
            for i in S[1:]:
                if i != Sbuffer:
                    new_string += i
                    Sbuffer = i
                else:
                    new_string = new_string[:-1]
                    Sbuffer = ' '
            numlist = [i for i in range(0, len(S) - 1)]
            list1 = list(filter(lambda x: S[x + 1] == S[x], numlist))
            if list1:
                S = new_string
            else:
                break
        return new_string
