# cook your dish here
testcases = int(input())
for x in range(testcases):
    size = int(input())
    li = list(map(int, input().split()))
    highmax = max(li)
    lowmin = min(li)
    new_list = set(li)
    new_list.remove(max(new_list))
    new_list.remove(min(new_list))
    secondhighmax = max(new_list)
    secondmin = min(new_list)
    print(highmax * secondhighmax, lowmin * secondmin)
