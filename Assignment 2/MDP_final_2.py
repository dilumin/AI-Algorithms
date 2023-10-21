
temp_map =  [[0,0,0],[0,0,0]]

map_v = [[0,0,0],[0,0,0]]
map_reward = [[-0.1,-0.1,-0.05],[-0.1,-0.1,1]]
Transition =[ 0.9,0.05 , 0.05]
gamma = 0.999




def move_up(location):
    if location[0] == 0 :
        return map_v[location[0]][location[1]]
    else:
        return map_v[location[0]-1][location[1]] 
def left(location):
    if location[1] == 0 :
        return map_v[location[0]][location[1]]
    else:
        return map_v[location[0]][location[1] - 1]

def right(location):
    if location[1] == len(map_v[0])-1 :
        return map_v[location[0]][location[1]]
    else:
        return map_v[location[0]][location[1]+1]
def down(location) :
    if location[0] == len(map_v)-1 :
        return map_v[location[0]][location[1]]
    else:
        return map_v[location[0]+1][location[1]]

    
for i in range (3):
    k =0

    for row in range(len(map_v)-1 ,-1 ,-1  ):
        for point in range (len(map_v[0])):
                
                if (i>0 and ((row == 1 and point == 2) )):
                    temp_map[row][point] = map_v[row][point]
                    k = k+ 1
                    print(k)
                    print("up:",1)
                    print("left:",1)
                    print("right:",1)
                    print("down:",1)
                    print("stay:",1)

                    print("max:",  1 ) 
                    # print(map_v[row][point])
                    continue
                up_1 =  (Transition[0] * map_reward[row][point] + 
                         Transition[0] * gamma * move_up([row, point]) + 
                         Transition[1] * map_reward[row][point] +
                         Transition[1] * gamma * left([row, point]) + 
                         Transition[2] * map_reward[row][point] +
                         Transition[2] * gamma * right([row, point]) )

    
                down_1 =(Transition[0] * map_reward[row][point] +Transition[0] * gamma * down([row, point]) +Transition[1] * map_reward[row][point] +Transition[1] * gamma * left([row, point]) +Transition[2] * map_reward[row][point] +Transition[2] * gamma * right([row, point]) )

                    
                left_1 =(Transition[0] * map_reward[row][point] +Transition[0] * gamma * left([row, point]) +Transition[1] * map_reward[row][point] +Transition[1] * gamma * down([row, point]) +Transition[2] * map_reward[row][point] +Transition[2] * gamma * move_up([row, point]) )

                    
                right_1 =(Transition[0] * map_reward[row][point] +Transition[0] * gamma * right([row, point]) +Transition[1] * map_reward[row][point] +Transition[1] * gamma * down([row, point]) +Transition[2] * map_reward[row][point] +Transition[2] * gamma * move_up([row, point]) )
                    
                stay = (map_reward[row][point] + gamma * map_v[row][point])
                
                temp_map[row][point] = max(up_1 , left_1 , right_1 , down_1 )
                k= k+ 1
                print(k)
                print("up:",up_1)
                print("left:",left_1)
                print("right:",right_1)
                print("down:",down_1)
                print("stay:",stay)

                print("max:",  max(up_1 , right_1  , down_1 , left_1) ) 
    map_v = temp_map
    temp_map = [[0,0,0],[0,0,0]]
    print("--")