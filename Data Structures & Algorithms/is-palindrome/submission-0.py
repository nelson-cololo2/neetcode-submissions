class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = "".join(ch for ch in s if ch.isalnum())
        chars = chars.lower()

        i = 0
        j = len(chars) - 1

        while i < j:
            if chars[i] != chars[j]:
                return False
            else:
                i += 1
                j -= 1
        return True