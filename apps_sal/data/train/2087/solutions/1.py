path = list(map(int, input().split()))
(n, L, R, QL, QR) = (path[0], path[1], path[2], path[3], path[4])
w = list(map(int, input().split()))
sumpref = [0]
for i in range(1, n + 1):
    sumpref.append(w[i - 1] + sumpref[i - 1])
answer = QR * (n - 1) + sumpref[n] * R
for i in range(1, n + 1):
    energy = L * sumpref[i] + R * (sumpref[n] - sumpref[i])
    if i > n - i:
        energy += (i - (n - i) - 1) * QL
    elif n - i > i:
        energy += (n - i - i - 1) * QR
    if answer > energy:
        answer = energy
print(answer)
