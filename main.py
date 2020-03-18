import sys

# Determine whether a one-to-one character mapping exists
def isOneToOne(str1, str2):

    hmap = {} # store the mapping relationship between str1 and str2

    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        cur = hmap.get(str1[i], 0)
        # not yet exist in hmap
        if cur == 0:
            hmap[str1[i]] = str2[j]
        # not one-to-one
        elif str2[j] != cur:
            return False
        i += 1
        j += 1
    
    return True

# Check input numbers
def inputNumCheck(num):
    if num > 3:
        print("ERROR : Must input only 'two' strings.")
        exit(1)


# Check input strings' length []
def lengthCheck(str1, str2):

    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        print("ERROR : The lengths of two strings should be equal.")
        exit(1)