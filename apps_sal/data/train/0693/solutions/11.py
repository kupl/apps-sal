# cook your dish here
t = int(input())
fact = [1,1]
for i in range(2,21):
    fact.append(i * fact[i - 1])
for i in range(t):
    n = int(input())
    print(fact[n])
