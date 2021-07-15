n1 = input()
# k = int(input())
n, k = map(int, n1.split())
main_lot = []
rel_mat = []
for i in range(n):
    x1 =[]
    for j in range(n):
        x1.append(0)
    rel_mat.append(x1)
for i in range(n):
    # print(i)
    rel_mat[i][i] = 1
# print(rel_mat)
for gen in range(n):
    length1 = list(map(int, input().split()))
    length1 = length1[1:]
    # print(length1)
    for lits in range(len(main_lot)):
        independentcunt = 0
        # main_lot[lits]
        for everyele in range(len(length1)):
            # length1[everyele]
            if length1[everyele] in main_lot[lits]:
                independentcunt += 1
        # print(independentcunt)
        if independentcunt>=k:
            rel_mat[gen][lits] = rel_mat[lits][gen] = 1
            pass
    main_lot.append(length1)
    pass


# print(n)
# print(k)

# print(main_lot)
# print(rel_mat)
fami_ly = []
unfam_ily = []
i1te = 0






while i1te<5:
    new_ele_rel = []
    for ele in rel_mat:
        temp1 = []
        for el1 in ele:
            temp1.append(el1)
        new_ele_rel.append(temp1)
    i1te+=1
    for lists1 in range(len(rel_mat)):
        
        unfam_ily = [i2 for i2 in range(n)]
        fami_ly = [i1 for i1 in range(len(rel_mat[lists1])) if rel_mat[lists1][i1] == 1 ]
        fami_ly.remove(lists1)
        unfam_ily.remove(lists1)
        for tem1 in fami_ly:
            unfam_ily.remove(tem1)
        unfami_ly = [i2 for i2 in range(len(rel_mat[lists1])) if rel_mat[lists1][i2] == 0 ]

        for iter1 in fami_ly:
            for iter2 in unfam_ily:
                if new_ele_rel[iter1][iter2] == 1:
                    # print("did reach")

                    new_ele_rel[iter2][lists1] = 1
                    new_ele_rel[lists1][iter2] = 1
                    # print(new_ele_rel[lists1][iter1])
                    # print(iter1,lists1)
                    # print(new_ele_rel)

                    pass 
                pass 
        #     pass
        # print(fami_ly)
        # print(unfam_ily)
        fami_ly = []
        unfam_ily = []

        # print(rel_mat)



count = sum(new_ele_rel[0])
print(count)




