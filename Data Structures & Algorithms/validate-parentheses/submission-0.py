class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False
        stack = []
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0 