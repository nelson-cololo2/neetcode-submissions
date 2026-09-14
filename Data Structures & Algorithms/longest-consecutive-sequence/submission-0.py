class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        best = 0

        for n in nums:
            if n - 1 in lookup:
                continue
            else:
                length = 1
                while (n + length) in lookup:
                    length += 1
                best = max(best, length)
        
        return best

        