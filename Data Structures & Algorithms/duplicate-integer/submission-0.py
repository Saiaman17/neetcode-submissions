class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenn = set()
        for i in nums:
            if i in seenn:
                return True
            seenn.add(i)
        return False