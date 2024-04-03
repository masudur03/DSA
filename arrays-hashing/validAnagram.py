def isAnagram(s, t):
    charSet = set()
    charSet.update(s)
    for char in t:
        if char not in charSet:
            return False
        # if all the char is in hashset
        return True


# using hashmap

def isAnagram2(s, t):
    if len(s) != len(t):
        return False
    # make hashmap in python, basically dictionary
    countS, countT = {}, {}

    # inputing the values and their count into the hashmap
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True
