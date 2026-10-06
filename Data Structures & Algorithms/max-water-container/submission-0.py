class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) -  1
        while left < right:
            width = right - left
            cur_height = min(heights[left],heights[right])
            area = width * cur_height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, area)
        return max_area