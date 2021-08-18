
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        min_length = 30
        index = -1
        for i in range(n):
            x = arr[i]
            if len(x) < min_length:
                index = i
                min_length = len(x)

        s = arr[index]
        answers = []
        l = len(s)
        while l > 0:
            for i in range(len(s)):
                if i + l > len(s):
                    break
                flag = True
                sub = s[i:i + l]

                for j in arr:
                    if j.find(sub) == -1:
                        flag = False
                        break
                if flag:
                    answers.append(sub)
            l -= 1
            if len(answers) > 0:
                break

        answers.sort()
        print((answers[0]))


main()
