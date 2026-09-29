class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        frq = {}
        for num in range(n):
            frq[nums[num]] = frq.get(nums[num], 0) + 1
        sort_seen = sorted(frq.items(),key = lambda item:item[1], reverse = True)
        return [item[0] for item in sort_seen[0:k]]