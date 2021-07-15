from math import ceil; makeParts=lambda arr, c: [arr[i*c:i*c+c] for i in range(ceil(len(arr)/c))]
