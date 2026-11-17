from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ## Use coutner function and put it into 
        countS = sorted(list(s))
        countT = sorted(list(t))

        return countS == countT
