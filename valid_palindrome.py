# ✅ Problem: Valid Palindrome
# 🔢 LeetCode #125
# 🔗 https://leetcode.com/problems/valid-palindrome/
# 📌 Assumptions:
#   - The string may contain spaces, punctuation, symbols
#   - We're to ignore all non-alphanumeric characters
#   - Comparisons should be **case-insensitive**
#   - An empty string is considered a palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Filter only alphanumeric characters and convert to lowercase
        cleaned = ''.join(char.lower() for char in s if char.isalnum())

        # Step 2: Check if cleaned string is same forward and backward
        return cleaned == cleaned[::-1]