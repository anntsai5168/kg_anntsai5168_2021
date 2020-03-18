"""
Title: Checking one-to-one character mapping
03/18/2021
Ming-Yun (Ann) Tsai

Description:
1. Use hash map to store the mapping relationship between 2 strings.
2. If there's a change happens, for example : 'a' -> 'b' to 'a' -> 'c', return False, otherwise, return True.
3. Handle input errors.
4. Time complexity : O(N) / Space complexity : O(N) [N: the size of the input strings]
"""

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


if __name__ == '__main__':

    # Check input numbers
    num = len(sys.argv)
    inputNumCheck(num)

    # Command Line Arguments
    str1 = sys.argv[1]
    str2 = sys.argv[2]

    # Check input strings' length
    lengthCheck(str1, str2)
        
    # Determine whether a one-to-one character mapping exists
    result = isOneToOne(str1, str2)
    print(result)