class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        res = []
        max_len = len(S) // 3 + 1
            
        def add_fibonacci(x, left):
            # print(x)
            # print(left)
            temp1 = x[0]
            temp2 = x[1]
            res = None
            res_left = left
            for i in range(len(left)):
                temp3 = int(left[:i + 1])
                if temp3 == temp1 + temp2 and temp3 < 2 ** 31 - 1:
                    # print(temp3)
                    res = temp3
                    res_left = res_left[i + 1:]
                    break
                elif temp3 > temp1 + temp2:
                    break
            # print(res, res_left)
            return res, res_left
            
        for i in range(1, max_len + 1):
            c1 = S[0:i]
            if len(c1) > 1 and c1[0] == '0':
                break
            for j in range(i + 1, max_len + i + 1):
                c2 =S[i:j]
                if len(c2) > 1 and c2[0] == '0':
                    break
                # next_length = max(len(c1), len(c2))
                next_index = j
                left = S[next_index:]
                res.append(int(c1))
                res.append(int(c2))
                while len(left) > 0:
                    # print(res)
                    # print(res[-2:])
                    temp, left = add_fibonacci(res[-2:], left)
                    if temp is None:
                        res.clear()
                        break
                    res.append(temp)
                #     print(res, left, len(left))
                # print(res)
                if len(res) > 0:
                    break
                res.clear()
            if len(res) > 0:
                break
            
            res.clear()
        return res
