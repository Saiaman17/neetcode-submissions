class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        res = ""
        for ch in s:
            if ch.isalnum():
                res += ch
        right = len(res) - 1
        while left < right:
            if res[left] != res[right]:
                return False
            else:
                left += 1
                right -= 1
        return True