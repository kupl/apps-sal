n, m = list(map(int, input().split()))
splFriends = input().split()
sppost = []
posts = []
for i in range(m):
    f, p, s = input().split()
    p = int(p)
    if f in splFriends:
        sppost.append([p, s])
    else:
        posts.append([p, s])
    sppost = sorted(sppost, key=lambda x: x[0])[::-1]
    posts = sorted(posts, key=lambda x: x[0])[::-1]

for post in sppost:
    print(post[1])
for post in posts:
    print(post[1])
