from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 in num_set:
                continue
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == '__main__':
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2, 2]
    result = solution.longestConsecutive(nums)
    print(result)
