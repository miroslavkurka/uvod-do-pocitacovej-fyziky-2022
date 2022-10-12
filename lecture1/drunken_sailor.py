import random as rd

def init_matrix(dimension):
    return [[0 for _ in range(dimension)]]*dimension


def sailor_populate(n):
    step = rd.randint(1,4)
    matrix= init_matrix(n)
    for i in range(len(matrix)):
        for j in range(len(matrix)):

    return matrix
def visualize_map(n):

    matrix= sailor_populate(n)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j],end='')
        print()
if __name__ == "__main__":
    visualize_map(5)
    pass    
