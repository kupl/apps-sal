class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:

        def impl(s, pos, output):
            if pos >= len(s):
                return len(output) >= 3
            loop_end = len(s) + 1
            if s[pos] == '0':
                loop_end = pos + 2
            for p in range(pos + 1, loop_end):
                this_number = int(s[pos:p])
                if this_number > pow(2, 31) - 1:
                    continue
                if len(output) >= 2 and output[-1] + output[-2] == this_number:
                    output.append(this_number)
                    if impl(s, p, output):
                        return True
                    else:
                        output.pop()
                elif len(output) < 2:
                    output.append(this_number)
                    if impl(s, p, output):
                        return True
                    else:
                        output.pop()
            return False

        result = []
        impl(S, 0, result)

        return result
