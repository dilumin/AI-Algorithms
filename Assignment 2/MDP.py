map_v = [[0,0,0],[0,0,0]]
map_reward = [[-0.1,-0.1,-0.05],[-0.1,-0.1,1]]
Transition =[ 0.9,0.05 , 0.05]
gamma = 0.999

Utility_directions =[0,0,0]


def move_up(location):
    if location[0] == 0:
        return map_v[location[0]][location[1]]
    else:
        return map_v[location[0]-1][location[1]]  # Replace parentheses with square brackets

def left(location):
    if location[1] == 0:
        return map_v[location[0]][location[1]]
    else:
        return map_v[location[0]][location[1] - 1]

def right(location):
    if location[1] == 2:
        return map_v[location[0]][location[1]]
    else:
        return map_v[location[0]][location[1]+1]

for i in range (3):
    for row in range(len(map_v)-1 ,0 ,-1 ):
        for point in range (len(map_v[row-1])):
                directions =[0,1,2]
                for direction in range (3):
                    Utility_directions[direction] = (
        Transition[directions[0]] * map_reward[row][point] +
        Transition[directions[0]] * gamma * move_up([row, point]) +
        Transition[directions[1]] * map_reward[row][point] +
        Transition[directions[1]] * gamma * left([row, point]) +
        Transition[directions[2]] * map_reward[row][point] +
        Transition[directions[2]] * gamma * right([row, point])
    )



                    
                    directions.append(directions.pop(0))
                map_v[row][point] = max(Utility_directions)

    print(map_v)