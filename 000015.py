class Solution(object):

    # 需要从剩余的数组片段start-end中找到和为-target的元素
    # 并且second和third都不能等于target，也不能相等
    def twoSum(self, nums, target, start, end):
        two_result = []
        # 双指针法
        left = start
        right = end
        while left < right:
            second = nums[left]
            third = nums[right]
            if second + third + target == 0:
                two_result.append([target, second, third])
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
            # 遍历first后面的数组片段找剩余的second和third
            two_result = self.twoSum(nums, nums[first], first + 1, n - 1)
            for i in two_result:
                result.append(i)
        return result


solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
result = solution.threeSum(nums)
print(result)
