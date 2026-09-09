class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def signature(word):
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            return tuple(freq)
        
        groups = {}

        for word in strs:
            x = signature(word)
            if x in groups:
                groups[x].append(word)
            else:
                groups[x] = [word]
        
        return list(groups.values())