import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

inf=float('inf')
class Node:
    def __init__(self,value):
        self.value=value
        self.nbrs=[]
    @staticmethod
    def addEdge(self,other,weight):
        self.nbrs.append([other,weight])
        other.nbrs.append([self,weight])

class Graph:
    def __init__(self,n):
        self.nodes=list(Node(i) for i in range(n))
    def addEdges(self):
        for t in range(int(input())):
            u,v,w=map(int,input().split())
            Node.addEdge(self.nodes[u],self.nodes[v],w)
    def printPaths(self):
        n=len(self.nodes)
        for i in range(n):
            print("Path cost:", self.sofar[i],end=" | ")
            print(i,end=" ")
            while self.parent[i]!=-1:
                i=self.parent[i]
                print("<--",i, end=" ")
            print()

    def Dijkstra(self,start):
        n=len(self.nodes)

        self.sofar=[inf for i in self.nodes]
        self.parent=[None for i in self.nodes]
        visited=[False for i in self.nodes]

        self.sofar[start]=0
        self.parent[start]=-1

        while start!=None:
            # print(start)
            # print(visited)
            # print(self.parent)
            # print(self.sofar)
            for v,w in self.nodes[start].nbrs:
                if self.sofar[v.value]==0:
                    continue
                if self.parent[v.value]==None or self.sofar[v.value]>w+self.sofar[start]:
                    self.parent[v.value]=start
                    self.sofar[v.value]=w+self.sofar[start]

            visited[start]=True
            start=None
            for u in range(n):
                if not visited[u]:
                    if not start:
                        start=u
                    elif self.sofar[u]<self.sofar[start]:
                        start=u




graph=Graph(int(input()))
graph.addEdges()
graph.Dijkstra(int(input()))
graph.printPaths()

