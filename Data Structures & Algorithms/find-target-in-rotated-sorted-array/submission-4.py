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
                l, r = pivot, len(nums) - 1

                while l <= r:
                    
                    mid = (l + r) // 2
                    if target == nums[mid]:
                        return mid
                    elif target > nums[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1

            else: 
                l, r = 0, pivot

                while l <= r: 
                    mid = (l + r) // 2
                    if target == nums[mid]:
                        return mid
                    elif target > nums[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
            
        return -1