from typing import List
import collections


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            # key = "".join(sorted(st))
            key = sorted(st)
            key = "".join(key)
            mp[key].append(st)

        return list(mp.values())


if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams(strs)
    print(result)  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
