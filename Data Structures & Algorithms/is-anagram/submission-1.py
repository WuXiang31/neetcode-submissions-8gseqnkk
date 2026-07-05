class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        #Base case, if the length is not the same
        #It can't be a anagram to each other
        if len(s) != len(t):
            return False

        #Sort the text of two side and compare the sort result
        if sorted(s) == sorted(t):
            return True
        else:
            return False