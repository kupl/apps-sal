# In this kata, you will write a function that returns the positions
# and the values of the "peaks" (or local maxima) of a numeric array.
# For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak
# at position 3 with a value of 5 (since arr[3] equals 5).
# The output will be returned as an object with two properties: pos and peaks.
# Both of these properties should be arrays. If there is no peak
# in the given array, then the output should be {pos: [], peaks: []}.
# Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
# should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)
# All input arrays will be valid integer arrays (although it could still
# be empty), so you won't need to validate the input.
# The first and last elements of the array will not be considered as peaks
# (in the context of a mathematical function, we don't know what is after
# and before and therefore, we don't know if it is a peak or not).
# Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while
# [1, 2, 2, 2, 3] does not. In case of a plateau-peak, please only
# return the position and value of the beginning of the plateau.
# For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]}
# (or equivalent in other languages)

def sign(x):
    if x>0:
       return 1
    elif x<0:
       return -1
    elif x==0:
       return 0

def pick_peaks(arr):
    pos = []
    peaks = []
    l = len(arr)
# Calculate differential array    
    diff_arr = []
    for i in range (0, l-1):
        diff_arr.append(sign(arr[i+1] - arr[i]))
# Pick_Peaks
    i = 0
    while i < l-2:
        k = 1
        while sign(diff_arr[i+k]) == 0 and i+k < l-2:
            k += 1
        if (sign(diff_arr[i+k]) < sign(diff_arr[i]) and
            sign(diff_arr[i]) != 0 and sign(diff_arr[i+k]) != 0):
                pos.append(i+1)
                peaks.append(arr[i+1])
        i += k
# Create Dictionary!        
    d_pos_peaks = dict(pos=pos, peaks=peaks)    
    return d_pos_peaks
