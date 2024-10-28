class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        for index in range(0, max(len(word1), len(word2))):
            letter1 = word1[index : index + 1] or ""
            letter2 = word2[index : index + 1] or ""
            new_string += letter1 + letter2
        return new_string


if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("first", "second"))
    print(s.mergeAlternately("sec", "first"))
