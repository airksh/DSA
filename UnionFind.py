# Optimized “Disjoint Set” with Path Compression and Union by Rank


# The main idea of a “disjoint set” is to have all connected vertices have the same parent node or root node, whether directly or indirectly connected. 
# To check if two vertices are connected, we only need to check if they have the same root node.
# The two most important functions for the “disjoint set” data structure are the find function and the union function. 
# The find function locates the root node of a given vertex. The union function connects two previously unconnected vertices by giving them the same root node. 
# There is another important function named connected, which checks the “connectivity” of two vertices. The find and union functions are essential for any question 
# that uses the “disjoint set” data structure.


class UnionFind():
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        root_x = self.root[x]
        root_y = self.root[y]
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
