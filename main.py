import matplotlib.pyplot as plt
import random
import math


class CityGrid:
    def __init__(self, n, m, coverage_threshold=0.3):
        self.n = n
        self.m = m
        self.grid = [[0] * m for _ in range(n)] 
        self.coverage_threshold = coverage_threshold
        self.place_obstructed_blocks()

    def place_obstructed_blocks(self):
        for i in range(self.n):
            for j in range(self.m):
                if random.random() < self.coverage_threshold:
                    self.grid[i][j] = 1 

    def display_grid(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))
            
    def place_tower(self, i, j, tower_range):
        for row in range(max(0, i - tower_range), min(self.n, i + tower_range + 1)):
            for col in range(max(0, j - tower_range), min(self.m, j + tower_range + 1)):
                if self.grid[row][col] == 0:
                    self.grid[row][col] = 2

    
    def find_coverage(self):
        towers = []
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == 0:
                    self.place_tower(i, j, 1)
                    towers.append((i, j))

        return towers
    def calculate_distance(self, tower1, tower2):
        x1, y1 = tower1
        x2, y2 = tower2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def find_reliable_path(self, tower1, tower2):
        if tower1 == tower2:
            return [tower1]

        path = [tower1, tower2]
        return path

    def visualize_path(self, path):
        plt.imshow(self.grid, cmap='Blues')
        plt.colorbar()
        plt.plot([pos[1] + 0.5 for pos in path], [pos[0] + 0.5 for pos in path], 'r.-')
        
        plt.show()
        
    def visualize_coverage(self):
        plt.imshow(self.grid, cmap='Blues')
        plt.colorbar()
        plt.show()
    # def find_coverage(self, tower_cost, budget):
    #     towers = []
    #     remaining_budget = budget

    #     while remaining_budget >= min(tower_cost.values()):
    #         best_coverage_increase = 0
    #         best_tower = None

    #         for i in range(self.n):
    #             for j in range(self.m):
    #                 if self.grid[i][j] == 0:
    #                     coverage_increase = self.calculate_coverage_increase(i, j, towers)
    #                     if coverage_increase > best_coverage_increase and tower_cost[(i, j)] <= remaining_budget:
    #                         best_coverage_increase = coverage_increase
    #                         best_tower = (i, j)

    #         if best_tower is None:
    #             break

    #         self.place_tower(best_tower[0], best_tower[1], 1)
    #         towers.append(best_tower)
    #         remaining_budget -= tower_cost[best_tower]

    #     return towers

    # def calculate_coverage_increase(self, i, j, towers):
    #     coverage_increase = 0
    #     for tower in towers:
    #         if self.calculate_distance((i, j), tower) <= 1:
    #             coverage_increase -= 1

    #     return coverage_increase

city = CityGrid(10, 10)
city.display_grid()

city.place_tower(3, 6, 2)
towers = city.find_coverage()
path = city.find_reliable_path(tower1=towers[0], tower2=towers[1])
city.visualize_path(path)
city.visualize_coverage()