'''
49. 字母异位词分组
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
'''

from typing import List
import collections


class Solution:
    '''
    复杂度分析
    时间复杂度：O(nklogk)，其中 n 是 strs 中的字符串的数量，k 是 strs 中的字符串的的最大长度。需要遍历 n 个字符串，对于每个字符串，需要 O(klogk) 的时间进行排序以及 O(1) 的时间更新哈希表，因此总时间复杂度是 O(nklogk)。
    空间复杂度：O(nk)，其中 n 是 strs 中的字符串的数量，k 是 strs 中的字符串的的最大长度。需要用哈希表存储全部字符串。
    '''

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            # key = "".join(sorted(st))
            key = sorted(st)
            key = "".join(key)
            mp[key].append(st)

        return list(mp.values())


solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solution.groupAnagrams(strs)
print(result)  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
