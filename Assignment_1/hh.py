import random

class Truck:
    def __init__(self, truck, map):
        self.no_of_stops = int(truck[-1])
        self.path = []
        self.name = truck[:-2]
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
b = [['0', '5', 'N', 'N', 'N', '6'], ['5', '0', '19', 'N', '15', 'N'], ['N', '19', '0', '22', 'N', '10'], ['N', 'N', '22', '0', '10', 'N'], ['N', '15', 'N', '10', '0', '12'], ['6', 'N', '10', 'N', '12', '0']]

len = b.__len__()

nodesIndeces =  list(range(len))
nodesIndeces.pop(0)
random.shuffle(nodesIndeces)
trucks = ['truck_1#2', 'truck_2#2' , 'truck_3#1']
t1 = Truck(trucks[0] , nodesIndeces )
t2 = Truck(trucks[1] , nodesIndeces )
t3 = Truck(trucks[2] , nodesIndeces )




print(calculate_shortest(t1,b) + calculate_shortest(t2,b) + calculate_shortest(t3,b))
print(t1.path)
print(t2.path)
print(t3.path)