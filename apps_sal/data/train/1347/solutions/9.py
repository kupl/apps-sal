n, m = list(map(int, input().split()))
friends = list(map(int, input().split()))
friendsPost = []
otherPost = []

for friend in range(m):

    f, p, s = list(map(str, input().split()))
    if int(f) in friends:

        friendsPost.append([f, int(p), s])

    else:

        otherPost.append([f, int(p), s])


friendsPost.sort(key=lambda x: x[1])
otherPost.sort(key=lambda x: x[1])

for post in range(len(friendsPost) - 1, -1, -1):
    print(friendsPost[post][-1])


for post in range(len(otherPost) - 1, -1, -1):
    print(otherPost[post][-1])
