class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

class Solution:
    def isValid(self, s: str) -> bool:
        o = {
            "}":"{",
            "]":"[",
            ")":"(",
        }
        stack = []

        for c in s:
            if c in o:
                if not (
                    stack
                    and (stack.pop() == o[c])
                ):
                    return False
            else:
                stack.append(c)
        return not stack
