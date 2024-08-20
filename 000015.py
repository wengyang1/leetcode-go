class Solution(object):

    # 需要从剩余的数组片段start-end中找到和为-target的元素
    # 并且second和third都不能等于target，也不能相等
    def twoSum(self, nums, target, start, end):
        two_result = []
        # 双指针法
        left = start
        right = end
        last_valid_second = float('inf')
        while left < right:
            second = nums[left]
            third = nums[right]
            if second + third + target == 0:
                # 排除重复答案，如果本次的第二个元素和上次的第二个元素相同，
                # 那么就是重复答案，双指针继续向内靠拢
                if not last_valid_second == second:
                    two_result.append([target, second, third])
                    last_valid_second = second
                left += 1
                right -= 1
            elif second + third + target > 0:
                right -= 1
            else:
                left += 1
        return two_result

    def threeSum(self, nums):
        result = []
        # 数组排序
        nums.sort()
        # 遍历数组找first元素
        n = len(nums)
        # n-2是因为至少要给后面留2个元素
        for first in range(n - 2):
            # 不可以包含重复的三元组，所以答案中的第一个元素不能重复
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # 遍历first后面的数组片段找剩余的second和third
            two_result = self.twoSum(nums, nums[first], first + 1, n - 1)
            for i in two_result:
                result.append(i)
        return result


solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
result = solution.threeSum(nums)
print(result)
