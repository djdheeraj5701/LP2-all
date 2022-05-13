import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Node:
    def __init__(self,value):
        self.value=value
        self.nbrs=[]
    @staticmethod
    def addEdge(self,other):
        self.nbrs.append(other)
        other.nbrs.append(self)

class Graph:
    colors = "Red Green Blue Orange".split()
    def __init__(self,n):
        self.nodes=list(Node(i) for i in range(n))
        self.allowed = dict()
        self.assigned = dict()
        self.count=0
        for i in range(n):
            self.allowed[i]=dict()
            for j in Graph.colors:
                self.allowed[i][j]=True
            self.assigned[i]=None
    def addEdges(self):
        for t in range(int(input())):
            u,v=map(int,input().split())
            Node.addEdge(self.nodes[u],self.nodes[v])
    def displayResults(self):
        self.count+=1
        for i in range(n):
            print(i,":",self.assigned[i])
        print()
    def assignTheColor(self,i,j):
        self.assigned[i]=j
        for v in self.nodes[i].nbrs:
            if not self.assigned[v.value]:
                self.allowed[v.value][j]=False
    def removeTheColor(self, i, j):
        self.assigned[i] = None
        for v in self.nodes[i].nbrs:
            if not self.assigned[v.value]:
                self.allowed[v.value][j] = True

    def coloring(self,i):
        if i==n:
            self.displayResults()
            return
        for j in self.allowed[i]:
            if self.allowed[i][j]:
                self.assignTheColor(i,j)
                self.coloring(i+1)
                self.removeTheColor(i, j)

n=int(input())
graph=Graph(n)
graph.addEdges()
graph.coloring(0)
print(graph.count)