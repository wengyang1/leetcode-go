class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        for right in range(n):
            # 这个while是关键，当右指针的字符跟前面的重复时，左指针就会一直向右移动，直到删除了重复的那个字符
            while s[right] in lookup:
                lookup.remove(s[left])
                left += 1
            lookup.add(s[right])
            max_len = max(max_len, len(lookup))
        return max_len


solution = Solution()
s = "pwwkew"
print(solution.lengthOfLongestSubstring(s))
