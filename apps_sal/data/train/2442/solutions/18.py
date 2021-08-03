class Solution:
    def sortString(self, s: str) -> str:
        output = []
        temp = list(s)
        dump = []

        while len(temp) > 0:
            temp.sort()
            output.append(temp[0])
            temp.remove(temp[0])
            for e in temp:
                if e > output[-1]:
                    output.append(e)
                    temp[temp.index(e)] = ''
            temp = [e for e in temp if e]

            if len(temp) == 0:
                break
            temp.reverse()
            output.append(temp[0])
            temp.remove(temp[0])
            for e in temp:
                if e < output[-1]:
                    output.append(e)
                    temp[temp.index(e)] = ''
            temp = [e for e in temp if e]

            print(output)

        return ''.join(output)
