class State:
    def __init__(self, north, east, south, west , stay):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.stay = stay
        self.best = max(north, east, south, west, stay)
        self.set_direction()

    def set_direction(self):
        if self.best == self.north:
            self.best = "north"
        elif self.best == self.east:
            self.best = "east"
        elif self.best == self.south:
            self.best = "south"
        else:
            self.best = "west"

        

def get_state_utilities (epsilon , map_reward ):
    Transition =[ 0.9,0.05 , 0.05]
    gamma = 0.999
    delta = epsilon * (1 - gamma) / gamma
    temp_map =  [[ State(0,0,0 ,0) ,State(0,0,0 ,0),State(0,0,0 ,0)],[State(0,0,0 ,0),State(0,0,0 ,0),State(0,0,0 ,0)]]
    map_v =  [[ State(0,0,0 ,0) ,State(0,0,0 ,0),State(0,0,0 ,0)],[State(0,0,0 ,0),State(0,0,0 ,0),State(0,0,0 ,0)]]

    def move_up(location):
        if location[0] == 0 :
            return map_v[location[0]][location[1]].best
        else:
            return map_v[location[0]-1][location[1]].best
    
    def left(location):
        if location[1] == 0 :
            return map_v[location[0]][location[1]].best
        else:
            return map_v[location[0]][location[1] - 1].best
    
    def right(location):
        if location[1] == len(map_v[0])-1 :
            return map_v[location[0]][location[1]].best
        else:
            return map_v[location[0]][location[1]+1].best
    
    def down(location) :
        if location[0] == len(map_v)-1 :
            return map_v[location[0]][location[1]].best
        else:
            return map_v[location[0]+1][location[1]].best

    max_diff = float("inf")
    i = -1
    while True:
        i = i + 1
        if max_diff < delta:
            break    
        k =0
        all_diff = []

        for row in range(len(map_v)-1 ,-1 ,-1  ):
            for point in range (len(map_v[0])):
                    
                    if (i>0 and ((row == 1 and point == 2) )):
                        temp_map[row][point] = map_v[row][point]

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
                    left_1 = round(left_1, 10)


                    right_1 = round(right_1, 10)
                    up_1 = round(up_1, 10)
                    down_1 = round(down_1, 10)
                    stay = round(stay, 10)
                    map_v[row][point].east = right_1
                    map_v[row][point].north = up_1
                    map_v[row][point].south = down_1
                    map_v[row][point].west = left_1
                    map_v[row][point].stay = stay
                    map_v[row][point].set_direction()
                    a = max(up_1 , left_1 , right_1 , down_1 )
                    difference = abs(map_v[row][point] - a)
                    temp_map[row][point] = a
                    all_diff.append(difference)


        map_v = temp_map
        max_diff = abs(max(all_diff))
        temp_map = [[0,0,0],[0,0,0]]
    return map_v

map_reward = [[-0.1,-0.1,-0.05],[-0.1,-0.1,1]]
epsilon = 0.01

print(get_state_utilities(epsilon , map_reward ))
