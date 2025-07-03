#  Problem: Valid Palindrome
#  LeetCode #125
#  Link: https://leetcode.com/problems/valid-palindrome/
#  Assumptions:
#   - Empty string is considered a valid palindrome
#   - Only alphanumeric characters should be considered (ignore spaces, punctuation)
#   - Case insensitive comparison (treat 'A' and 'a' as equal)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Remove non-alphanumeric characters and convert to lowercase
        cleaned = ''.join([char.lower() for char in s if char.isalnum()])

        # Step 2: Compare cleaned string to its reverse
        return cleaned == cleaned[::-1]