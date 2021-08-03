maxLead = 0
a_sum = 0
b_sum = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    a_sum += a
    b_sum += b
    if(a_sum > b_sum):
        lead = a_sum - b_sum
        if lead > maxLead:
            maxLead = lead
            w = 1
    else:
        lead = b_sum - a_sum
        if(lead > maxLead):
            maxLead = lead
            w = 2
print(w, maxLead)
