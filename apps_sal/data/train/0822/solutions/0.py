def main():
        while True:
                [n, m] = [int(i) for i in input().split()]
                if n == m and n == 0:
                        break
                cache = {}
                for i in range(n):
                        dna = input().rstrip('\n')
                        if dna in cache:
                                cache[dna] = 1 + cache[dna]
                        else:
                                cache[dna] = 1
                c = [0 for i in range(n + 1)]
                for dna in cache:
                        c[cache[dna]] = 1 + c[cache[dna]]
                for i in range(1, n + 1):
                        print(c[i])
 
def __starting_point():
        main()
__starting_point()
