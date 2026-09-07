class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for n in nums:
            s[n] = s.get(n, 0) + 1
        x = sorted(s.keys(), key=lambda x: s[x], reverse=True)
        return x[:k]
        

