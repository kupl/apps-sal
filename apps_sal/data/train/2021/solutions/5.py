def IsPossible(graph, n, color, start, isVisited):
    stack = [start]

    while stack != []:
        #print (color)
        curr = stack.pop()
        if (not isVisited[curr - 1]) and (graph[curr] != []):
            isVisited[curr - 1] = True
            if color[curr - 1] == 0:
                color[curr - 1] = 1
                for kid in graph[curr]:
                    color[kid - 1] = 2
            elif color[curr - 1] == 1:
                for kid in graph[curr]:
                    if color[kid - 1] == 0 or color[kid - 1] == 2:
                        color[kid - 1] = 2
                    else:
                        return []
            else:
                for kid in graph[curr]:
                    if color[kid - 1] == 0 or color[kid - 1] == 1:
                        color[kid - 1] = 1
                    else:
                        return []
            for kid in graph[curr]:
                stack.append(kid)

    return color


def Solve(color):
    first = []
    second = []

    for i in range(len(color)):
        if color[i] == 1:
            first.append(i + 1)
        elif color[i] == 2:
            second.append(i + 1)

    fstr = ''
    sstr = ''
    for i in first:
        fstr += str(i) + ' '

    for i in second:
        sstr += str(i) + ' '

    print(len(first))
    print(fstr)
    print(len(second))
    print(sstr)


def main():
    n, m = list(map(int, input().split()))
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    for i in range(m):
        start, end = list(map(int, input().split()))
        graph[start].append(end)
        graph[end].append(start)

    color = [0] * n
    isVisited = [False] * n
    for i in range(n):
        color = IsPossible(graph, n, color, i + 1, isVisited)
        if color == []:
            print(-1)
            return
    Solve(color)


main()
