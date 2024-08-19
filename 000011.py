class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            lh = height[left]
            rh = height[right]
            area = min(lh, rh) * (right - left)
            max_area = max(area, max_area)
            if lh < rh:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_area = solution.maxArea(height)
    print(max_area)  # 49
