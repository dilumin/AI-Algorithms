map_v = [[0,0,0],[0,0,0]]
temp_map =  [[0,0,0],[0,0,0]]
map_reward = [[-0.1,-0.1,-0.05],[-0.1,-0.1,1]]
Transition =[ 0.9,0.05 , 0.05 , -1 , 1]
gamma = 0.999

Utility_directions =[ 0, 0, 0, 0,0 ]



def move_up(location):
    if location[0] == 0:
        return map_v[location[0]][location[1]]
    else:
        return map_v[location[0]-1][location[1]] 
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
def down(location):
    if location[0] == 1:
        return map_v[location[0]][location[1]]
    else:
        return map_v[location[0]+1][location[1]]


for i in range (3):
    for row in range(len(map_v)-1 ,-1 ,-1 ):
        for point in range (len(map_v[row-1])):
                    up_1 =  (
        Transition[0] * map_reward[row][point] +
        Transition[0] * gamma * move_up([row, point]) +
        Transition[1] * map_reward[row][point] +
        Transition[1] * gamma * left([row, point]) +
        Transition[2] * map_reward[row][point] +
        Transition[2] * gamma * right([row, point]) 

    )
                    down_1 =(
        Transition[0] * map_reward[row][point] +
        Transition[0] * gamma * down([row, point]) +
        Transition[1] * map_reward[row][point] +
        Transition[1] * gamma * left([row, point]) +
        Transition[2] * map_reward[row][point] +
        Transition[2] * gamma * right([row, point]) 

                    )
                    left_1 =(
        Transition[0] * map_reward[row][point] +
        Transition[0] * gamma * left([row, point]) +
        Transition[1] * map_reward[row][point] +
        Transition[1] * gamma * down([row, point]) +
        Transition[2] * map_reward[row][point] +
        Transition[2] * gamma * move_up([row, point]) 

                    )
                    right_1 =(
        Transition[0] * map_reward[row][point] +
        Transition[0] * gamma * right([row, point]) +
        Transition[1] * map_reward[row][point] +
        Transition[1] * gamma * down([row, point]) +
        Transition[2] * map_reward[row][point] +
        Transition[2] * gamma * move_up([row, point]) )
                    
                    stay = (
                         map_reward[row][point] + gamma * map_v[row][point]
                    )
                
                    temp_map[row][point] = max(up_1 , left_1 , right_1 , down_1 )

                    print(up_1 , right_1  , down_1 , left_1 ,stay) 
    map_v = temp_map
    print("--")