import numpy as np
from scipy.spatial.distance import cdist
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

xs, xy, xt, yt = map(int, input().split())
N = int(input())
barriers = np.array([(xs, xy, 0), (xt, yt, 0)] + [tuple(map(int, input().split())) for _ in range(N)])
dist = cdist(barriers[:, :2], barriers[:, :2])
dist = np.maximum(dist - barriers[:, 2] - barriers[:, 2][:, None], 0)

length = dist.ravel()
frm = np.repeat(np.arange(N + 2), N + 2)
to = np.tile(np.arange(N + 2), N + 2)

matr = csr_matrix((length, (frm, to)), shape=(N + 2, N + 2))
ans = dijkstra(matr, indices=0)[1]
print(ans)
