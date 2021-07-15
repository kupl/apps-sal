def find_in_array(seq, predicate):
        l=[i for i,value in enumerate(seq) if predicate(value,i)]
        return l[0] if l else -1
