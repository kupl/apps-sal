import re


def no_order(s):
    try:
        nums = [int(i.replace(' ', '')) for i in re.split('\+|\-|\*|\/|\^|\%', s)]
        ops = [a for a in s if not a in nums and not a in ' 1234567890']
        ans = nums[0]
        for n in range(1, len(nums)):
            op = ops[n - 1]
            num = nums[n]
            if op == '+':
                ans += num
            if op == '-':
                ans -= num
            if op == '*':
                ans *= num
            if op == '/':
                ans = ans // num
            if op == '^':
                ans = ans ** num
            if op == '%':
                ans = ans % num
        return ans
    except:
        return None
