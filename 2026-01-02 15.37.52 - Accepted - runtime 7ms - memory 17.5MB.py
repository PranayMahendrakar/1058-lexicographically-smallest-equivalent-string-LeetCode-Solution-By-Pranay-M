class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Union-Find with path compression
        # Parent array - each char maps to its parent
        parent = list(range(26))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                # Always make the smaller one the parent
                if px < py:
                    parent[py] = px
                else:
                    parent[px] = py
        
        # Build equivalence relations
        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))
        
        # Build result
        result = []
        for c in baseStr:
            result.append(chr(find(ord(c) - ord('a')) + ord('a')))
        
        return ''.join(result)