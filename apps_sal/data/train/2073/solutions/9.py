def fun(numbers):
    le = len(numbers)
    stack = []
    ans = 0
    i = 1
    for i in numbers:
        while stack:
            ans = max(ans, stack[-1] ^ i)
            if stack[-1] > i:
                break
            else:
                stack.pop()
        stack.append(i)

    return ans


n = input()
user_input = input().split(' ')
numbers = [int(x.strip()) for x in user_input]

print(fun(numbers))
