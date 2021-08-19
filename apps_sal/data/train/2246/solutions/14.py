import heapq


def smaller_by_1(num):
    return num - 1


def main():
    (N, k) = list(map(int, input().split(' ')))
    X = list(map(int, input().split(' ')))
    A = int(input())
    C = list(map(int, input().split(' ')))
    money_needed = 0
    drinks_needed = []
    drunk_to_now = 0
    for i in range(N):
        objective = X[i]
        drinks_needed.append((objective - k + A - 1) // A)
    possible_drinks = []
    for i in range(len(drinks_needed)):
        heapq.heappush(possible_drinks, C[i])
        if drinks_needed[i] - drunk_to_now <= 0:
            continue
        else:
            while drinks_needed[i] - drunk_to_now != 0:
                if len(possible_drinks) == 0:
                    print(-1)
                    return 0
                else:
                    money_needed += heapq.heappop(possible_drinks)
                    drunk_to_now += 1
    print(money_needed)


main()
