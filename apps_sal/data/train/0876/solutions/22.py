from sys import stdout, stdin


def main():
    numOfKids, difference = list(map(str, input().split()))
    numbers = [int(x) for x in stdin.readline().split()]
    numOfKids = int(numOfKids)
    difference = int(difference)
    smallest = largest = numbers[0]
    for j in range(1, len(numbers)):
        if (smallest > numbers[j]):
            smallest = numbers[j]
            min_position = j
        if (largest < numbers[j]):
            largest = numbers[j]
            max_position = j
    listDiff = largest - smallest
    if(listDiff > difference):
        print("NO")
    elif(difference > listDiff):
        print("YES")
    elif(difference == listDiff):
        print("NO")


def __starting_point():
    testCases = int(stdin.readline())
    if 0 <= testCases <= 100:
        for _ in range(testCases):
            main()


__starting_point()
