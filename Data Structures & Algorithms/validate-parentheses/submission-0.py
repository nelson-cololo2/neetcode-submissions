class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else None
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0
        