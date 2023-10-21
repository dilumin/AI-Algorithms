import random

class Truck:
    def __init__(self, truck, map):
        self.no_of_stops = int(truck[-1])
        self.path = []
        for i in range(0, self.no_of_stops):
            self.path.append(map.pop(0))
        print(self.path)
    


def shortest_dist(start, end, graph):
    num_nodes = graph.__len__()
    shortest_distances = [float('inf')] * num_nodes
    shortest_distances[start] = 0

    visited = [False] * num_nodes

    for _ in range(num_nodes):
        min_distance = float('inf')
        min_node = -1

        for node in range(num_nodes):
            if not visited[node] and shortest_distances[node] < min_distance:
                min_distance = shortest_distances[node]
                min_node = node

        if min_node == -1:
            break

        visited[min_node] = True

        for neighbor in range(num_nodes):
            if (
                not visited[neighbor]
                and graph[min_node][neighbor] != 'N'
                and shortest_distances[neighbor] > shortest_distances[min_node] + int(graph[min_node][neighbor])
            ):
                shortest_distances[neighbor] = shortest_distances[min_node] + int(graph[min_node][neighbor])

    return shortest_distances[end]





def calculate_shortest(truck ,map ):
    closest_node = 0
    tot_dist = 0
    closest_node_dist = 100
    temp = []
    start_node = 0
    
    while True:
        
        
        
        for node in truck.path:
            dist = shortest_dist(start_node , node , map)

            if dist < closest_node_dist:
                closest_node = node
                closest_node_dist = dist
        
        truck.path.remove(closest_node)
        temp.append(closest_node)
        tot_dist += closest_node_dist
        closest_node_dist = 100
        start_node = closest_node
        if truck.path.__len__() == 0:
            truck.path = temp
            break
    return tot_dist
# Open the file for reading
a = []
with open("input.txt", "r") as input_file:
    a = input_file.readline().split(',')
len = a.__len__()
# print(len)  # 10

b =[]

open_file = open("input.txt", "r")
for i in range (0 , len):
    a = open_file.readline().strip().split(',')
    b.append(a)
trucks =[]
while(True):
    a = open_file.readline().strip()
    if a == '':
        break
    trucks.append(a)

len = b.__len__()

nodesIndeces =  list(range(len))
nodesIndeces.pop(0)
random.shuffle(nodesIndeces)
t1 = Truck(trucks[0] , nodesIndeces )
t2 = Truck(trucks[1] , nodesIndeces )

calculate_shortest(t1,b)