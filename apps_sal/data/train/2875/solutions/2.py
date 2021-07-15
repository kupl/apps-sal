def sort_photos(pics):
    out = sorted(pics, key=lambda i: (int(i[:4]), int(i.split('g')[-1])))[:-6:-1][::-1]
    out.append(out[-1].split('g')[0] + 'g' + str(int(out[-1].split('g')[-1])+1))
    return out
