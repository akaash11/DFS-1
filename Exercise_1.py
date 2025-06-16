# S30 Problem #64 Flood fill
#LeetCode #733 https://leetcode.com/problems/flood-fill/description/

# Author : Akaash Trivedi
# Time Complexity : O(m * n)
# Space Complexity : O(m * n)
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

# DFS solution
# from start position check for neighbors and update the color then recursively do it for other

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or len(image) == 0: return image
        initcolor = image[sr][sc]
        # the start point color is same as target color, nothing to do
        if initcolor == color:
            return image
        # directions array - Right Botton Left Top
        drcn = [[1,0],[0,-1],[-1,0],[0,1]]
        self.dfs(image, sr, sc, color, initcolor, drcn)
        return image

    def dfs(self, image, cr, cc, color, initcolor, drcn):
        # base
        # In DFS we check the opposite conditions
        if cr < 0 or cc < 0 or cr >= len(image) or cc >= len(image[0]) or image[cr][cc] != initcolor:
            return
        # logic
        image[cr][cc] = color
        for dr in drcn:
            nr = cr + dr[0]
            nc = cc + dr[1]
            self.dfs(image, nr, nc, color, initcolor, drcn)

# BFS solution
# from start position check for neighbors and update the color then add it to the queue

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or len(image) == 0: return image
        m = len(image)
        n = len(image[0])
        initcolor = image[sr][sc]
        # the start point color is same as target color, nothing to do
        if initcolor == color:
            return image
        queue = deque()
        queue.append(sr)
        queue.append(sc)
        # directions array - Right Botton Left Top
        drcn = [[1,0],[0,-1],[-1,0],[0,1]]

        while queue:
            cr = queue.popleft() # curr row
            cc = queue.popleft() # curr column
            image[cr][cc] = color
            # check neighbors
            for dr in drcn:
                nr = cr + dr[0] # new row idx
                nc = cc + dr[1] # new col idx
                # bound check for corners
                if nr>=0 and nc >=0 and nr < m and nc < n and image[nr][nc] == initcolor:
                    image[nr][nc] = color
                    queue.append(nr)
                    queue.append(nc)
        return image