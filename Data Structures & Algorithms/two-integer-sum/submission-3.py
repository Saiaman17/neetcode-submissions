class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        summ = 0
        for i in range(n):
            for j in range(i+1 , n):
                summ = nums[i] + nums[j]
                if summ == target:
                    return [i,j] if i < j else [j,i]