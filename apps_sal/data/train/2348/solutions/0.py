N = int(input())
X = list(map(int, input().split()))
L = int(input())


def one_step(i):
    goal = X[i] + L

    # find largest j s.t. X[j] <= X[i] + L
    low = 0
    high = N
    while high - low > 1:
        mid = (high + low) // 2
        if X[mid] <= goal:
            low = mid
        else:
            high = mid

    return low


onesteps = [one_step(i) for i in range(N)]


def double(layer):
    return [layer[layer[i]] for i in range(N)]


NUM_LAYERS = 20
layers = [onesteps]
for _ in range(NUM_LAYERS):
    layers.append(double(layers[-1]))


def query(a, b):
    if a > b:
        a, b = b, a

    ans = 0
    while a < b:
        ind = 0
        while layers[ind + 1][a] < b:
            ind += 1
        ans += 2 ** ind
        a = layers[ind][a]
    return ans


Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(query(a, b))
