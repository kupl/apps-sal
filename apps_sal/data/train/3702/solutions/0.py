def olympic_ring(string):
    return (['Not even a medal!'] * 2 + ['Bronze!', 'Silver!', 'Gold!'])[min(4, sum(map('abdegopqABBDOPQR'.count, string)) // 2)]
