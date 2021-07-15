# cook your dish here
N = int(input())
matches = list(map(int,input().split()))
games = matches[:3]
for i in range(3,N):
    games.append(min(games[i-1],games[i-2],games[i-3]) + matches[i])
print(sum(matches) - min(games[-1],games[-2],games[-3]))


