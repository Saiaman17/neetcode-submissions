class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n == 0:
            return []
        res = set()
        for i in range(n - 2):
            left, right = i + 1 , n - 1
            while left < right:
                tot = nums[i] + nums[left] + nums[right]
                if tot == 0:
                    res.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
                if tot < 0:
                    left += 1
                if tot > 0:
                    right -= 1
        return [list(tri) for tri in res]