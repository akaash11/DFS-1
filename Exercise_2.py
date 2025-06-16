# S30 Problem #65
#LeetCode #542 https://leetcode.com/problems/01-matrix/description/

# Author : Akaash Trivedi
# Time Complexity : O(m * n)
# Space Complexity : O(m * n)
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        drcn = [[1,0],[0,-1],[-1,0],[0,1]]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = -1
                else:
                    queue.append([i,j])
        dist = 1
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                for dr in drcn:
                    nr = curr[0] + dr[0]
                    nc = curr[1] + dr[1]
                    if nr >= 0 and nc >= 0 and nr < m and nc < n and mat[nr][nc] == -1:
                        mat[nr][nc] = dist
                        queue.append([nr,nc])
            dist += 1
        
        return mat