"""
TC: (k ^ n)-> (k^(N/k))
k = average length of each group
n: height of tree : number of groups
n = N/k
N: lenght of given list
"""


class Solution:

    def dfs(self, idx, groups, path):

        # base case
        if idx >= len(groups):
            str_ = "".join(path)
            self.ans.append(str_)
            return

            # logic
        grp_len = len(groups[idx])
        # traverse the ith group
        for i in range(grp_len):
            path.append(groups[idx][i])
            self.dfs(idx + 1, groups, path)
            path.pop()

    def expand(self, s: str) -> List[str]:
        self.ans = []
        groups = []
        n = len(s)
        idx = 0
        while idx < n:
            lst = []
            if s[idx] == "{":
                idx += 1
                while s[idx] != "}":
                    if s[idx] != ",":
                        lst.append(s[idx])
                    idx += 1
                idx += 1
                lst.sort()
            else:
                lst.append(s[idx])
                idx += 1
            groups.append(lst)

        # idx is the index of group
        self.dfs(0, groups, [])
        return self.ans


