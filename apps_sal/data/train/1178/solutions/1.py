test_case = int(input())
while test_case:
    n = int(input())
    friends_req = list(map(int, input().strip().split()))
    friends_req.sort()
    current_friends = 0
    for i in range(n):
        if friends_req[i] <= current_friends:
            current_friends += 1
        else:
            break
    print(current_friends)
    test_case -= 1
