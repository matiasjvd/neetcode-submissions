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
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []
        strings = strs.copy()
        bans = []
        for string in strs:
                
            if string  not in bans:
                anagrams = []
                anagrams.append(string)
                strings.remove(string)

                for comparison in strings:

                    if self.isAnagram(string, comparison):
                        anagrams.append(comparison)
                        anagrams = sorted(anagrams)
                        bans.append(comparison)
                            
                output.append(anagrams)

        return output


        