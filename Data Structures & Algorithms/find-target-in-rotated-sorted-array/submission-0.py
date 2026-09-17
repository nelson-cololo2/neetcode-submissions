class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums:
            left, right = 0, len(nums) - 1

            while left < right:
                mid = (left + right) // 2

                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
                
            pivot = left
            
            if target >= nums[pivot] and target <= nums[-1]:
                for i in range(pivot, len(nums)):
                    if target == nums[i]:
                        return i
                return -1
            else:
                for i in range(pivot):
                    if target == nums[i]:
                        return i
                return -1
        return -1     