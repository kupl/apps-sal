class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hash_table={}
        invalid=[]
        index=-1
        lindex=[]
        for trans in transactions:
            count_coma=0
            word=''
            name=''
            dl=[]
            index+=1
            lenght=0
            ind=0
            for l in trans:
                lenght+=1
                if l==',' or lenght==len(trans):
                    count_coma+=1
                    if count_coma==1:
                        name=word
                    elif count_coma==2:
                        tl=[int(word)]
                        dl.append(tl)
                    elif count_coma==3:
                        if int(word)>1000:
                            ind=1
                    else:
                        cl=[word]
                        dl.append(cl)
                        dl.append([index])
                        if name not in hash_table:
                            hash_table[name]=dl
                            if ind==1:
                                invalid.append(trans)
                                lindex.append(index)
                        else:
                            if ind==1:
                                invalid.append(trans)
                                lindex.append(index)
                            for i in range(0,len(hash_table.get(name)[0])):
                                if abs(hash_table.get(name)[0][i]-dl[0][0])<61 and hash_table.get(name)[1][i]!=dl[1][0]:
                                    if index not in lindex:
                                        invalid.append(trans)
                                        lindex.append(index)
                                    if hash_table.get(name)[2][i] not in lindex:
                                        invalid.append(transactions[hash_table.get(name)[2][i]])
                                        lindex.append(hash_table.get(name)[2][i])
                            hash_table.get(name)[0].append(dl[0][0])
                            hash_table.get(name)[1].append(dl[1][0])
                            hash_table.get(name)[2].append(index)
                    word=''
                else:
                    word+=l
        return invalid

