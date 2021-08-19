n = int(input())
balance = list(map(int, input().split()))
q = int(input())
log = [list(map(int, input().split())) for i in range(q)]
ind_of_last_operation = [None] * n
max_pay = 0
ind_of_max_payment = None
payments = []
payments_id = []
for i in range(q):
    if log[i][0] == 1:
        ind_of_last_operation[log[i][1] - 1] = i
for i in range(q):
    if log[i][0] == 2:
        ind_of_last_payment = i
        last_payment = log[i][1]
        if log[i][1] > max_pay:
            max_pay = log[i][1]
max_pay_for_moment = [0] * (q + 1)
for j in range(q - 1, -1, -1):
    if log[j][0] == 2:
        max_pay_for_moment[j] = max(log[j][1], max_pay_for_moment[j + 1])
    else:
        max_pay_for_moment[j] = max_pay_for_moment[j + 1]
for i in range(n):
    if ind_of_last_operation[i] == None:
        if balance[i] < max_pay:
            balance[i] = max_pay
    elif max_pay_for_moment[ind_of_last_operation[i] + 1] > log[ind_of_last_operation[i]][2]:
        balance[i] = max_pay_for_moment[ind_of_last_operation[i] + 1]
    else:
        balance[i] = log[ind_of_last_operation[i]][2]
print(*balance)
