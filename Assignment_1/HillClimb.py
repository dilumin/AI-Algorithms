import random


#class for a truck to store its name, assigned stops and shortest path crossing those cities
class Truck:
    def __init__(self, truck, map):
        self.no_of_stops = int(truck[-1])
        self.name = truck[:-2]
        self.path = []
        self.shortest_path = [0]
        for i in range(0, self.no_of_stops):  #a truck is assigned cities to visit , in the path list
            self.path.append(map.pop(0))
    
#function that returns ac true for a given probability
def probability_function(p):
    return random.random() < p

#function to calculate shortest distance between two nodes and the shortest path between them
def shortest_dist(start, end, graph):
    num_nodes = graph.__len__()
    shortest_distances = [float('inf')] * num_nodes
    shortest_distances[start] = 0
    predecessors = [-1] * num_nodes 

    visited = [False] * num_nodes
    
    for _ in range(num_nodes):
        min_distance = float('inf')
        min_node = -1
    #
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
                predecessors[neighbor] = min_node  

    path = []
    current_node = end
    while current_node != -1:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()  

    return shortest_distances[end], path



#function to calculate shortest path for a truck
#For a randomly assigned cities for a truck,it finds the shortest path between the cities using Dijkstra's algorithm
def calculate_shortest(truck,map ):

    closest_node = 0
    tot_dist = 0
    closest_node_dist = float('inf')
    temp = []
    start_node = 0
    
    while True:

        for node in truck.path:
            #we make start city as the city we are currently in
            dist ,path = shortest_dist(start_node , node , map)
               #In a assigned cities, from the starting city we find the closest city and we visit that city and check for the next closest city
               #this way we can find the shortest path covering all the randomly assigned cities
            if dist < closest_node_dist:

                shortest_path1 = [start_node]
                closest_node = node
                closest_node_dist = dist
                if shortest_path1[-1] == path[0]:
                    path.pop(0)
                
                shortest_path1.extend(path)
                
        
        truck.path.remove(closest_node)
        temp.append(closest_node)
        tot_dist += closest_node_dist
        if truck.shortest_path[-1] == shortest_path1[0]:
            shortest_path1.pop(0)
        truck.shortest_path.extend(shortest_path1)
        closest_node_dist = float('inf')
        start_node = closest_node  # we visit the next closest city and start from the top of the  loop to check the next closest city
        if truck.path.__len__() == 0:
            truck.path = temp
            break
    return tot_dist


#Openning a file to get the Input
#first checking the number of destination cities + start city 
a = []
with open("input.txt", "r") as input_file:
    a = input_file.readline().split(',')
len = a.__len__()

#inputting the map
map1 =[]

open_file = open("input.txt", "r")
for i in range (0 , len):
    a = open_file.readline().strip().split(',')
    map1.append(a)

#inputting the truck details
trucks =[]
while(True):
    a = open_file.readline().strip()
    if a == '':
        break
    trucks.append(a)




#we make a list with all the cities (these cities names are 1,2,3,4,5,6 . 1 repesenting b , 2 representing c and so on)
nodesIndeces =  list(range(len))
nodesIndeces.pop(0)

min = float('inf')
count = 0
bestTruck = []  #to store the states of the best trucks for a given input

t = 0  #for iterations
while True:
    t+=1
    random.shuffle(nodesIndeces)  #we shuffle the order of the cities
    truck_list = [] #we make a list with all the trucks as Truck objects
    for i in range(0, trucks.__len__()):
        truck_list.append(Truck(trucks[i], nodesIndeces)) 
    #when making the truck objects each truck object is assigned with random cities. No two truck is assigned with the same city
    
    costs =[] #a list to append the cost for each truck for a given instance (for the assigned random list of cities)
    for i in range(0, trucks.__len__()):
        costs.append(calculate_shortest(truck_list[i], map1))
    
    

    sum_cost = sum(costs) #sum of all costs of all trucks for a assigned set of random cities for each truck

    #Hill Climbing 

    if ( sum_cost < min ):  #if this total cost is better than the last cost we set it as the best case

        bestTruck = truck_list
        min = sum_cost
    elif  (probability_function( (10/t))): #if the currently randomized assigned way is not that good we may also set it as the best case with a probability that lowers with each iteration
        bestTruck = truck_list
        min = sum_cost
    elif probability_function(0.00001 * t): # otherwise we may stop and display the current solution as the best solution with a probability that increases with the iteration
        break
        

    nodesIndeces =  list(range(len)) #we remake the list with cities to be shuffled in the upcoming iteration
    nodesIndeces.pop(0)

#outputing the best solution in a file
file_write = open("210102D.txt", "w")
for truck1 in bestTruck:
    file_write.write(truck1.name + '#')
    for loc in range(1, truck1.shortest_path.__len__()):
        file_write.write(chr(truck1.shortest_path[loc] +97))
        if loc != truck1.shortest_path.__len__()-1:
            file_write.write(',')
    file_write.write('\n')
file_write.write(str(min))


