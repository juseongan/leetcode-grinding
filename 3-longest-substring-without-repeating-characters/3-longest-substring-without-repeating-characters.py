class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        record = 0
        
        left = 0
        for right in range(len(s)):
            while s[right] in charSet: # slide left edge until duplicate is removed
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right]) # slide the right edge of the window
            
            record = max(record, right - left + 1)
            
        return record