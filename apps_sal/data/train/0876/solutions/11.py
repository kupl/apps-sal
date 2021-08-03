# cook your dish here
t = int(input())
while t > 0:
    n, x = map(int, input().split())
    candies = list(map(int, input().split()))
    max_candies = max(candies)
    min_candies = min(candies)
    if(max_candies - min_candies < x):
        print("YES")
    else:
        print("NO")
    t -= 1
