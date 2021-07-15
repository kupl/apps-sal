def args_to_string(A):
    return ' '.join(e if isinstance(e, str) else e[0] if len(e)==1 else '-'+(len(e[0])>1)*'-' +' '.join(e) for e in A)
