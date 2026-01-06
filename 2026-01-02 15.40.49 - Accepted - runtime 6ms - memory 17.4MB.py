class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if px < py:
                    parent[py] = px
                else:
                    parent[px] = py
        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))
        return ''.join(chr(find(ord(c) - ord('a')) + ord('a')) for c in baseStr)