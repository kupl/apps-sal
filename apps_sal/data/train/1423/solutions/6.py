for case in range(int(input())):
    n = int(input())
    lengths = list(map(int, input().split()))
    k = int(input())
    uncle_song_len = lengths[k - 1]
    lengths.sort()
    print(lengths.index(uncle_song_len) + 1)
