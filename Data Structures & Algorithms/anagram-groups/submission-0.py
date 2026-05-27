class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = []
        used = set()

        for i in range(len(strs)):
            if i in used:
                continue

            anagram = [strs[i]]
            used.add(i)

            for j in range(i + 1, len(strs)):
                if self.isAnagram(strs[i], strs[j]):                    
                    anagram.append(strs[j])
                    used.add(j)
            group_anagram.append(anagram)
        return group_anagram        

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT