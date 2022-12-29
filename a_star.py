from collections import deque

class Graph:
    def __init__(self, list):
        self.list = list

    def get_neighbors(self, v):
        return self.list[v]
    
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }

        return H[n]
    
    def algo(self, start, stop):
        open_list = set([start])
        closed_list = set([])

        dist = {}
        dist[start] = 0

        adj_dist = {}
        adj_dist[start] = start

        while len(open_list) > 0:
            n = None
            
            for i in open_list:
                if n == None or dist[i] + self.h(i) < dist[n] + self.h(n):
                    n = i
            
            if n == None:
                print('Path doesn\'t exist')
                return None
            
            if n == stop:
                reconst_path = []

                while adj_dist[n] != n:
                    reconst_path.append(n)
                    n = adj_dist[n]
                
                reconst_path.append(start)
                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path
            
            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    adj_dist[m] = n
                    dist[m] = dist[n] + weight
                else:
                    if dist[m] > dist[n] + weight:
                        dist[m] = dist[n] + weight
                        adj_dist[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            
            open_list.remove(n)
            closed_list.add(n)
        print('Path doesn\'t exist')
        return None

nodes = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

graph = Graph(nodes)
graph.algo('A', 'D')