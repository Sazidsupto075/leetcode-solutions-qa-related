# ✅ Problem: Reverse String
# 🔢 LeetCode #344
# 🔗 Link: https://leetcode.com/problems/reverse-string/
# 📌 Assumptions:
#   - The input is a list of characters (e.g., ['h','e','l','l','o'])
#   - You must reverse it **in-place** (modify original list)
#   - Use O(1) extra memory (no new arrays or slicing allowed)
#   - You don't return anything — the original list should be updated directly

class Solution:
    def reverseString(self, s: List[str]) -> None:

        left,right = 0, len(s)-1

        while left< right:
            # swap characters from left to right
            s[left], s[right] = s[right], s[left]

            # MOve pointers inward

            left = left + 1
            right = right -1

            