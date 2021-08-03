def correct(R, C, Q):
    Q = list(map(int, Q))
    r = next((F for F, V in enumerate(Q[-R - C:-C]) if 1 & sum(Q[F * C:-~F * C]) ^ int(V)), -1)
    c = next((F for F, V in enumerate(Q[-C:]) if 1 & sum(Q[F:R * C:C]) ^ int(V)), -1)
    if 0 <= r or 0 <= c:
        Q[r - R - C if c < 0 else c + (-C if r < 0 else r * C)] ^= 1
    return ''.join(map(str, Q))
