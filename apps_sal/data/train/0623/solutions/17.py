def sort_array(array):
    array.sort()
    for i in range(len(array)):
        print(array[i])


t = int(input())
array = []
for _ in range(t):
    inp = int(input())
    array.append(inp)
sort_array(array)
