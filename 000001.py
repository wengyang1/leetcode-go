from typing import List


class Solution:
    # 暴力枚举，时间复杂度O(N2)
    def twoSumN2(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

    # 时间复杂度O(N1),借助哈希表
    def twoSumN1(self, nums: List[int], target: int) -> List[int]:
        # 创建一个哈希表，用于存储已遍历元素的值和对应的索引
        num_dict = {}

        # 遍历数组
        for i, num in enumerate(nums):
            # 计算差值
            complement = target - num

            # 检查差值是否已存在于哈希表中
            if complement in num_dict:
                # 如果存在，则返回当前索引和哈希表中差值的索引
                return [num_dict[complement], i]

                # 如果差值不存在，则将当前元素的值和索引存入哈希表
            num_dict[num] = i

            # 如果没有找到这样的两个数（理论上这行代码不会被执行）
        return []


solution = Solution()

# 定义输入数组和目标值
nums = [2, 7, 11, 15]
target = 9

# 调用twoSum方法并打印结果
result_n2 = solution.twoSumN2(nums, target)
print(result_n2)
result_n1 = solution.twoSumN1(nums, target)
print(result_n1)
