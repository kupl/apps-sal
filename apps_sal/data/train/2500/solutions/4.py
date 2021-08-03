class Solution:
    def maxPower(self, s: str) -> int:
        power = 1
        max_power = 0
        for idx, i in enumerate(s):
            if len(s) < 2:
                return len(s)
            if idx == 0:
                pass
            elif i == s[idx - 1]:
                power += 1
                print(f' i is {i}, power is {power}')
            else:
                print(f' i is {i}, power is {power}')
                if power > max_power:
                    max_power = power
                power = 1
        return max(power, max_power)
