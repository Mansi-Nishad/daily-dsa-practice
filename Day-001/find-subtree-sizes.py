#3331. Find Subtree Sizes After Changes
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        last = [-1] * 26
        new_parent = parent[:]
        stack = [(0, 0, -1)]

        while stack:
            node, state, prev = stack.pop()
            idx = ord(s[node]) - ord('a')

            if state == 0:
                prev = last[idx]

                if node != 0 and prev != -1:
                    new_parent[node] = prev

                last[idx] = node
                stack.append((node, 1, prev))

                for child in children[node]:
                    stack.append((child, 0, -1))
            else:
                last[idx] = prev

        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [1] * n
        order = [0]

        for node in order:
            for child in new_children[node]:
                order.append(child)

        for node in reversed(order[1:]):
            ans[new_parent[node]] += ans[node]

        return ans
