import random

class Truck:
    def __init__(self, truck, map):
        self.no_of_stops = int(truck[-1])
        self.path = []
        self.shortest_path = [0]
        for i in range(0, self.no_of_stops):
            self.path.append(map.pop(0))
    




def shortest_dist(start, end, graph):
    num_nodes = graph.__len__()
    shortest_distances = [float('inf')] * num_nodes
    shortest_distances[start] = 0
    predecessors = [-1] * num_nodes  # Initialize predecessors array

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
                predecessors[neighbor] = min_node  # Update predecessor

    # Reconstruct the shortest path
    path = []
    current_node = end
    while current_node != -1:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()  # Reverse the path to get it in the correct order

    return shortest_distances[end], path




def calculate_shortest(truck ,map ):

    closest_node = 0
    tot_dist = 0
    closest_node_dist = 100
    temp = []
    start_node = 0
    
    while True:
                
        for node in truck.path:
            
            dist ,path = shortest_dist(start_node , node , map)

            if dist < closest_node_dist:

                shortest_path1 = [start_node]
                closest_node = node
                closest_node_dist = dist
                if shortest_path1[-1] == path[0]:
                    path.pop(0)
                
                shortest_path1.extend(path)
                # truck.shortest_path.append(path) 
                
        
        truck.path.remove(closest_node)
        temp.append(closest_node)
        tot_dist += closest_node_dist
        if truck.shortest_path[-1] == shortest_path1[0]:
            shortest_path1.pop(0)
        truck.shortest_path.extend(shortest_path1)
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

min = 1000
count = 0
list_n =[]

for inn in  range(1000):
    random.shuffle(nodesIndeces)
    trucks = ['truck_1#2', 'truck_2#3' ]
    t1 = Truck(trucks[0] , nodesIndeces )
    t2 = Truck(trucks[1] , nodesIndeces )


    k1 = int(calculate_shortest(t1,b))
    k2 = int( calculate_shortest(t2,b))

    if ( k1 + k2  < min ):
        min = (k1 + k2 )
    if (k1 + k2  == 46):

        count += 1
    list_n.append(k1 + k2 )
        

    nodesIndeces =  list(range(len))
    nodesIndeces.pop(0)
    print(t1.shortest_path)
    print(t2.shortest_path)
    print(t1.path)
    print(t2.path)
# print(t1.path)
print(min)
print(count)
    # print(list_n)




# for inn in  range(10):
#     nodesIndeces = list(range(len))
#     random.shuffle(nodesIndeces)
#     # nodesIndeces = [2 , 4 , 1 , 5 ,3]
#     trucks = ['truck_1#2', 'truck_2#3' ]
#     t1 = Truck(trucks[0] , nodesIndeces )
#     t2 = Truck(trucks[1] , nodesIndeces )
#         # t3 = Truck(trucks[2] , nodesIndeces )

#     min1 = int(calculate_shortest(t1,b))
#     min2 = int(calculate_shortest(t2,b))

#     if ( min1 + min2  < min ):
#         min = (min1 + min2 )
#     if (min1 + min2  == 46):

#         count += 1
#     list_n.append(min1 + min2 )
        
#         # print(calculate_shortest(t1,b) + calculate_shortest(t2,b) + calculate_shortest(t3,b))
#         # print(t1.path)
#         # print(t2.path)
#         # print(t3.path)
#     nodesIndeces =  list(range(len))
#     nodesIndeces.pop(0)
#     print(t1.shortest_path)
#     print(t2.shortest_path)
#     print(t1.path)
#     print(t2.path)
#     print(min1+min2)
# # print(t1.path)
# print(min)
#     # print(count)
#     # print(list_n)

