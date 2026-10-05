class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        seen = set(nums)
        cur_seq = 1
        lon_seq = 0
        cur_num = 0
        for i in seen:
            if i - 1 not in seen:
                cur_num = i
                cur_seq = 1
            while cur_num + 1 in seen:
                cur_seq += 1
                cur_num += 1
            lon_seq = max(lon_seq,cur_seq)
        return lon_seq 