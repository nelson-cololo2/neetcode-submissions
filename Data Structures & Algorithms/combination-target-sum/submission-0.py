class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, total):
            # If we hit target, record the path
            if total == target:
                result.append(path[:])
                return
            
            # If we exceed the target, stop exploring
            if total > target:
                return
            
            # Explore choices starting from index 'start'
            for i in range(start, len(nums)):
                num = nums[i]

                # Choose the number
                path.append(num)

                # Since we can reuse nums[i], we pass i (not i+1)
                backtrack(i, path, total + num)

                # Undo the choice
                path.pop()
        backtrack(0, [], 0)
        return result