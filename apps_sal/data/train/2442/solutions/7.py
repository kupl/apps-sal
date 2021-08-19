class Solution:

    def sortString(self, s: str) -> str:
        output = []
        temp = sorted(list(s))
        while len(temp) > 0:
            output.append(temp[0])
            temp.remove(temp[0])
            for e in temp:
                if e > output[-1]:
                    output.append(e)
                    temp[temp.index(e)] = ''
            temp = [e for e in temp if e]
            if len(temp) == 0:
                break
            output.append(temp[-1])
            temp.remove(temp[-1])
            for i in range(len(temp) - 1, 0, -1):
                if temp[i] < output[-1]:
                    output.append(temp[i])
                    temp[i] = ''
            temp = [e for e in temp if e]
        return ''.join(output)
