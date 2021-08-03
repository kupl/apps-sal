class Solution:
    def sortString(self, s: str) -> str:
        output = []
        total = sorted(list(s))
        direction = 1
        while(len(total) > 0):
            if(direction == 1):
                selection = sorted(set(total))
            else:
                selection = sorted(set(total), reverse=True)
            direction *= -1
            output = output + list(selection)
            for char in selection:
                total.remove(char)
        return ''.join(output)
