class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words)==len(pattern):
            if len(set(words))==len(set(pattern)):
                paired = list(zip(pattern, words))
                if len(set(pattern))==len(set(paired)):
                    return True
                else:
                    return False
            else:
                return False

                