# Main maut ko takiya, aur kafan ko chaadar banakar audhta hoon!

s = input()

ans = 0

for i in range(len(s)):

    if(s[i] == 'A'):
        ql = s[:i].count("Q")
        qr = s[i + 1:].count("Q")

        ans += ql * qr

print(ans)
