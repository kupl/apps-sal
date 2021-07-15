def solution(digits):
    ans = []
    for i in range(0, len(digits)-4):
        ans.append(int(digits[i:i+5]))
    return max(ans)

