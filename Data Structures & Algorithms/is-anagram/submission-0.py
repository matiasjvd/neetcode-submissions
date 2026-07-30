class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

    #We can create add 1 value in the for and drop in the lists until their are empty if not they are not anagrams
        for string in s:
            if string in t:
                t = t.replace(string, "", 1)
                s = s.replace(string, "", 1)

        if s == "" and t == "":
            return True
        
        return False
        