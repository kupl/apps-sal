from collections import Counter

def get_key_length(cipher_text, max_key_length):
    avg_IC_by_keylen = {}
    
    for key_len in range(1, max_key_length+1):
        ICs = []
        
        for i in range(key_len):
            sub_str = cipher_text[i::key_len]
            freq = Counter(sub_str)
            IC = sum(v * (v-1) for k, v in freq.items()) / (len(sub_str) *  (len(sub_str)-1) )
            ICs.append(IC)
        
        avg_IC_by_keylen[key_len] = sum(ICs) / key_len
    
    return max(avg_IC_by_keylen, key=avg_IC_by_keylen.get)
