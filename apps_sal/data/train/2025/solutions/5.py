import math
import array


def is_prime(x):
    i = 2
    while(i <= math.sqrt(x)):
        if(x % i == 0):
            return False
        i = i + 1
    return True


answer_list = []
primel = [0 for c in range(1000)]
prime = array.array('i', primel)
n = int(input())
i = 2
answer = 0
while(i <= n):
    if(prime[i - 1] == 1):
        i = i + 1
        continue
    if(is_prime(i)):
        answer = answer + 1
        answer_list.append(i)
        prime[i - 1] = 1
        j = i * i
        while(j <= n):
            prime[j - 1] = 1
            answer = answer + 1
            answer_list.append(j)
            j = j * i
    i = i + 1
print(answer)
for x in answer_list:
    print(x, end=' ')
