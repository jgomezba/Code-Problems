import random

class Solver:
    def __init__(self, dimension:tuple = (4,8)):
        self.dimension = dimension
        self.positions = []
        self.visited_positions = []
        self.current_pos = (None,None)

    def get_all_positions(self):
        for x in range(self.dimension[0]):
            for y in range(self.dimension[1]):
                self.positions.append((x,y))

    def get_possible_movements(self, current_position:tuple):
        x = current_position[0]
        y = current_position[1]

        knight_movements = [(x+2,y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1),
                     (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]

        available_movements = [x for x in knight_movements if (x not in self.visited_positions) and (x in self.positions)]

        return available_movements
    
    def get_starter_point(self):
        starter = random.choice(self.positions)
        self.visited_positions.append(starter)
        
        self.positions.remove(starter)

        self.current_pos = starter

    def run(self, max_iters = 1000000):
        current_iter = 0
        game_end = False

        while (current_iter <= max_iters) and (not game_end):
            print("Iteration: ", current_iter)
            ended_tour = False
            self.positions = []
            self.visited_positions = []

            self.get_all_positions()
            self.get_starter_point()

            while not ended_tour:
                movements = self.get_possible_movements(self.current_pos)

                if movements == []:
                    ended_tour = True
                    continue

                movement = random.choice(movements)

                self.positions.remove(movement)
                self.visited_positions.append(movement)
                self.current_pos = movement
                
                if self.positions == []:
                    ended_tour = True
                    game_end = True
                    print("You won !")
                    return(self.visited_positions)
                
            current_iter +=1

        return None



if __name__ == "__main__":
    Slv = Solver()
    result = Slv.run()
    print(result)