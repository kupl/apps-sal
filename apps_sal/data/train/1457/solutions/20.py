# Note that it's python3 Code. Here, we are using input() instead of raw_input().
# You can check on your local machine the version of python by typing "python --version" in the termi
n, k = list(map(int, input().split()))
sum = 0
for i in range(n):
    if int(input()) % k == 0:
        sum += 1
print(sum)
