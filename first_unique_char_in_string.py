# ✅ Problem: First Unique Character in a String
# 🔢 LeetCode #387
# 🔗 Link: https://leetcode.com/problems/first-unique-character-in-a-string/
# 📌 Assumptions:
#   - The input string consists of lowercase English letters
#   - Return the index of the first non-repeating character
#   - If no such character exists, return -1

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count occurrences of each character
        freq = Counter(s)

        # Step 2: Loop through string to find the first unique character
        for index, char in enumerate(s):
            if freq[char] == 1:
                return index

        # Step 3: If no unique character found
        return -1