def main():
    left = -1
    right = -1
    edges = {}
    s = input()

    for i in range(len(s)):
        edges[i + 1] = right
        edges[left] = i + 1
        if s[i] == 'l':
            right = i + 1
        else:
            left = i + 1

    curr = edges[-1]
    while curr != -1:
        print(curr)
        curr = edges[curr]


main()
