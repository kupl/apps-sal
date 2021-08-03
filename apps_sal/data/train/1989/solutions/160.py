from collections import defaultdict


class Solution:
    def longestAwesome(self, s: str) -> int:
        def isPalindrome(dic, l, r):
            odds = set()
            length = 0
            for k, v in list(dic.items()):
                if v % 2 == 1:
                    odds.add(k)
                length += v
            # print(odds)
            if len(odds) == 0 or len(odds) == 1:
                return length
            elif len(odds) == 2:
                for num in odds:
                    if num == l or num == r:
                        return length - 1
                return 0
            elif len(odds) == 3:
                flag = 0
                for num in odds:
                    if num == l or num == r:
                        flag += 1
                if flag == 2:
                    return length - 2
                else:
                    return 0
            else:
                return 0

        def compact(s):
            numbers = []
            counts = []
            for num in s:
                if len(numbers) == 0 and len(counts) == 0:
                    numbers.append(num)
                    counts.append(1)
                    continue
                if num == numbers[-1]:
                    counts[-1] += 1
                else:
                    numbers.append(num)
                    counts.append(1)
            return numbers, counts

        def rollingHash(numbers, counts, l):
            anss = []
            dic = defaultdict(int)
            cur_max = 0
            max_acc = 0
            for i in range(l):
                num = numbers[i]
                cnt = counts[i]
                dic[num] += cnt
                max_acc += cnt
            cur_max = max(cur_max, max_acc)
            anss.append(isPalindrome(dic, numbers[0], numbers[l - 1]))
            for i in range(l, len(numbers)):
                l_num = numbers[i - l]
                l_cnt = counts[i - l]
                dic[l_num] -= l_cnt
                r_num = numbers[i]
                r_cnt = counts[i]
                dic[r_num] += r_cnt
                max_acc -= l_cnt
                max_acc += r_cnt
                cur_max = max(cur_max, max_acc)
                # print(dic, numbers[i-l+1], r_num, i - l + 1, i, numbers[i-l+1], r_num)
                anss.append(isPalindrome(dic, numbers[i - l + 1], r_num))
                # print(anss)
            return max(anss), cur_max

        numbers, counts = compact(s)
        cur_max = 0
        for l in range(len(numbers), 0, -1):
            # print(l, numbers, counts)
            new_max, max_acc = rollingHash(numbers, counts, l)
            # print(new_max, max_acc)
            cur_max = max(cur_max, new_max)
            if cur_max >= max_acc:
                return cur_max
        return 1
