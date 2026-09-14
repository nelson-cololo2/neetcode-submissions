class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
            x = str(len(word)) + "#"
            result.append(x + word)
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # 1. Read the full length (could be multiple digits)
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])   # substring from i to j (exclusive)

            # 2. Read the next <length> characters as the word
            word_start = j + 1
            word_end = j + 1 + length
            word = s[word_start:word_end]

            result.append(word)

            # 3. Move pointer to the next encoded segment
            i = word_end

        return result
