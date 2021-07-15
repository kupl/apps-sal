ring = "abdegopqADOPQR"

def olympic_ring(stg):
    score = sum(1 if c in ring else 2 if c == "B" else 0 for c in stg) // 2
    return "Gold!" if score > 3 else "Silver!" if score > 2 else "Bronze!" if score > 1 else "Not even a medal!"
