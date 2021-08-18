from sys import stdin, stdout
from collections import defaultdict
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    lst = list(map(int, stdin.readline().split()))
    prefix_odd = [0] * n
    prefix_even = [0] * n
    odd_val = 0
    even_val = 0
    for i in range(n):
        if lst[i] % 2 == 0:
            even_val += 1
        else:
            odd_val += 1
        prefix_even[i] = even_val
        prefix_odd[i] = odd_val
    prefix_sum = [0] * n
    s = 0
    for i in range(n):
        s += lst[i]
        prefix_sum[i] = s
    dict = {}
    count = {}
    for i in range(n):
        if lst[i] not in dict:
            dict[lst[i]] = i
            count[lst[i]] = 1
        else:
            dict[lst[i]] = i
            count[lst[i]] += 1
    graph = defaultdict(list)
    for i in range(n):
        graph[lst[i]].append(i)
    max_sum = 0
    for i in graph:
        if len(graph[i]) > 1:
            prev = graph[i][0]
            for j in range(1, len(graph[i])):
                index2 = graph[i][j]
                index1 = prev
                prev = index2
                if i % 2 == 0:
                    val = prefix_even[index2] - prefix_even[index1] - 1
                    if val % 2 == 0:
                        temp_sum = prefix_sum[index2] - prefix_sum[index1] - i
                        if temp_sum > max_sum:
                            max_sum = temp_sum
                else:
                    val = prefix_odd[index2] - prefix_odd[index1] - 1
                    if val % 2 != 0:
                        temp_sum = prefix_sum[index2] - prefix_sum[index1] - i
                        if temp_sum > max_sum:
                            max_sum = temp_sum

    '''max_sum=-1
                for i in range(n):
                    if count[lst[i]]>1:
                        index2=dict[lst[i]]
                        index1=i
                        print(index1,index2)
                        if lst[i]%2==0:
                            val=prefix_even[index2]-prefix_even[index1]-1
                            print(val)
                            if val%2==0:
                                temp_sum=prefix_sum[index2]-prefix_sum[index1]-lst[i]
                                print(temp_sum)
                                if temp_sum>max_sum:
                                    max_sum=temp_sum
                        else:
                            val=prefix_odd[index2]-prefix_odd[index1]-1
                            print(val)
                            if val%2!=0:
                                temp_sum=prefix_sum[index2]-prefix_sum[index1]-lst[i]
                                print(temp_sum)
                                if temp_sum>max_sum:
                                    max_sum=temp_sum'''

    stdout.write(str(max_sum) + '\n')
