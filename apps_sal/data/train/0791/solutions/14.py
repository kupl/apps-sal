t = int(input())
for i in range(t):
    (n, d) = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    sum = 0
    for j in arr:
        sum += j
    if sum % n != 0:
        print('-1')
    else:
        tmp = 0
        avg = sum / n
        num = [0] * d
        cnt = [0] * d
        for j in range(n):
            num[j % d] += arr[j]
            cnt[j % d] += 1
        for j in range(d):
            if num[j] % cnt[j] != 0 or num[j] / cnt[j] != avg:
                tmp = 1
                break
        if tmp:
            print('-1')
        else:
            ans = 0
            for j in range(n):
                if arr[j] < avg:
                    tmp = avg - arr[j]
                    ind = j + d
                    if ind < n and arr[ind] > 0:
                        ans += tmp
                        arr[j] = avg
                        arr[ind] -= tmp
                elif arr[j] > avg:
                    tmp = arr[j] - avg
                    ind = j + d
                    if ind < n:
                        ans += tmp
                        arr[j] = avg
                        arr[ind] += tmp
            print(ans)
"\n\nChef's dog Snuffles has so many things to play with! This time around, Snuffles \xa0\xa0\xa0\xa0has an array A containing N integers: A1, A2, ..., AN.\n\nBad news: Snuffles only loves to play with an array in which all the elements \xa0\xa0\xa0\xa0are equal.\n\nGood news: We have a mover of size D. !\n\nA mover of size D is a tool which helps to change arrays. Chef can pick two \xa0\xa0\xa0\xa0existing elements Ai and Aj from the array, such that i + D = j and subtract \xa0\xa0\xa0\xa01 from one of these elements \n(the element should have its value at least 1), and add 1 to the other element. \xa0\xa0\xa0\xa0In effect, a single operation of the mover, moves a value of 1 from one of \xa0\xa0\xa0\xa0the elements to the other.\n\nChef wants to find the minimum number of times she needs to use the mover of \xa0\xa0\xa0\xa0size D to make all the elements of the array A equal. Help her find this out\xa0\xa0\xa0\xa0.\n\nInput\nThe first line of the input contains an integer T, denoting the number of test \xa0\xa0\xa0\xa0cases. The description of T test cases follows.\nThe first line of each test case contains two integers N and D, denoting the \xa0\xa0\xa0\xa0number of elements in the array and the size of the mover.\nThe second line of each testcase contains N space-separated integers: A1, A2, \xa0\xa0\xa0\xa0..., AN, denoting the initial elements of the array.\n\nOutput\nFor each test case, output a single line containing the minimum number of uses \xa0\xa0\xa0\xa0or -1 if it is impossible to do what Snuffles wants.\n\nConstraints\n1 ≤ T ≤ 10\n2 ≤ N ≤ 10^5\n1 ≤ D < N\n1 ≤ Ai ≤ 10^9\n\nSubtasks\nSubtask 1 (30 points) : N ≤ 10^3\nSubtask 2 (70 points) : Original constraints\n\nExample\nInput:\n3\n5 2\n1 4 5 2 3\n3 1\n1 4 1\n4 2\n3 4 3 5\n\nOutput:\n3\n2\n-1\n\nExplanation\nTestcase 1:\nHere is a possible sequence of usages of the mover:\nMove 1 from A3 to A1\nMove 1 from A3 to A1\nMove 1 from A2 to A4\nAt the end, the array becomes (3, 3, 3, 3, 3), which Snuffles likes. And you \xa0\xa0\xa0\xa0cannot achieve this in fewer moves. Hence the answer is 3.\n\nTestcase 2:\nHere is a possible sequence of usages of the mover:\nMove 1 from A2 to A1\nMove 1 from A2 to A3\nAt the end, the array becomes (2, 2, 2), which Snuffles likes. And you cannot \xa0\xa0\xa0\xa0achieve this in fewer moves. Hence the answer is 2.\n\nTestcase 3:\nIt is impossible to make all the elements equal. Hence the answer is -1.\n\n"
