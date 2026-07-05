class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        #Base case, if the length is not the same
        #It can't be a anagram to each other
        if len(s) != len(t):
            return False


        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Check the hash value
        for c in countS:
            if countS.get(c) != countT.get(c):
                return False
        #If everythings is pass        
        return True
            
        

            
        