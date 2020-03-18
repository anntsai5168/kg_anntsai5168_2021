import collections

def isOneToOne(str1, str2):

    hmap = {}

    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        cur = hmap.get(str1[i], 0)
        # non exist
        if cur == 0:
            hmap[str1[i]] = str2[j]
        # not one to one
        elif str2[j] != cur:
            return False
        i += 1
        j += 1
    
    return True