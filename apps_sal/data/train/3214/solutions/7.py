def change(st):
    ze = '00000000000000000000000000'
    ze_li = list(ze)
    if 'a' in st.lower(): 
        ze_li[0] = '1'
    if 'b' in st.lower(): 
        ze_li[1] = '1'
    if 'c' in st.lower(): 
        ze_li[2] = '1'
    if 'd' in st.lower(): 
        ze_li[3] = '1'
    if 'e' in st.lower(): 
        ze_li[4] = '1'
    if 'f' in st.lower(): 
        ze_li[5] = '1'
    if 'g' in st.lower(): 
        ze_li[6] = '1'
    if 'h' in st.lower(): 
        ze_li[7] = '1'
    if 'i' in st.lower(): 
        ze_li[8] = '1'
    if 'j' in st.lower(): 
        ze_li[9] = '1'
    if 'k' in st.lower(): 
        ze_li[10] = '1'
    if 'l' in st.lower(): 
        ze_li[11] = '1'
    if 'm' in st.lower(): 
        ze_li[12] = '1'
    if 'n' in st.lower(): 
        ze_li[13] = '1'
    if 'o' in st.lower(): 
        ze_li[14] = '1'
    if 'p' in st.lower(): 
        ze_li[15] = '1'
    if 'q' in st.lower(): 
        ze_li[16] = '1'
    if 'r' in st.lower(): 
        ze_li[17] = '1'
    if 's' in st.lower(): 
        ze_li[18] = '1'
    if 't' in st.lower(): 
        ze_li[19] = '1'
    if 'u' in st.lower(): 
        ze_li[20] = '1'
    if 'v' in st.lower(): 
        ze_li[21] = '1'
    if 'w' in st.lower(): 
        ze_li[22] = '1'
    if 'x' in st.lower(): 
        ze_li[23] = '1'
    if 'y' in st.lower(): 
        ze_li[24] = '1'
    if 'z' in st.lower(): 
        ze_li[25] = '1'
    return ''.join(ze_li)
