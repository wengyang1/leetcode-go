from typing import List


class Solution(object):
    # 这个是我自己想的方法，但是时间复杂度很高，测试用例不通过，原因还没有找到
    def findAnagrams1(self, s, p):
        result = []
        # 这是获取字符串哈希值很常用的方法
        p_key = "".join(sorted(p))
        lp = len(p)
        for i in range(len(s) - lp + 1):
            s_key = "".join(sorted(s[i:i + lp]))
            if s_key == p_key:
                result.append(i)
        return result

    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)
        # 这个思路真不错：s先算出跟p一样的子串中字母的个数，然后后面循环的时候，再去掉左边的字母，
        # 这样就不用每次都把子串都遍历一次
        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1

            if s_count == p_count:
                ans.append(i + 1)

        return ans


solution = Solution()
s = "aaabb"
p = "bb"
print(solution.findAnagrams(s, p))
