class RubiksCube:
    def __init__(self):
        self.cube = {
            'U': [['W']*3 for _ in range(3)],
            'D': [['Y']*3 for _ in range(3)],
            'L': [['G']*3 for _ in range(3)],
            'R': [['B']*3 for _ in range(3)],
            'F': [['R']*3 for _ in range(3)],
            'B': [['O']*3 for _ in range(3)],
        }

    def display(self):
        for face in ['U', 'L', 'F', 'R', 'B', 'D']:
            print(face)
            for row in self.cube[face]:
                print(' '.join(row))
            print()

    def rotate_face_clockwise(self, face):
        self.cube[face] = list(zip(*reversed(self.cube[face])))

    def rotate_face_counterclockwise(self, face):
        self.cube[face] = list(reversed(list(zip(*self.cube[face]))))

    def rotate_U_clockwise(self):
        self.rotate_face_clockwise('U')
        temp_row = list(self.cube['F'][0])
        self.cube['F'][0] = self.cube['L'][0]
        self.cube['L'][0] = self.cube['B'][2][::-1]
        self.cube['B'][2] = self.cube['R'][0][::-1]
        self.cube['R'][0] = temp_row

    def rotate_U_counterclockwise(self):
        self.rotate_face_counterclockwise('U')
        temp_row = list(self.cube['F'][0])
        self.cube['F'][0] = self.cube['R'][0]
        self.cube['R'][0] = self.cube['B'][2][::-1]
        self.cube['B'][2] = self.cube['L'][0][::-1]
        self.cube['L'][0] = temp_row

    # Add more functions for other moves (e.g., D, L, R, F, B rotations)

# Example usage:
cube = RubiksCube()
cube.display()
cube.rotate_U_clockwise()
cube.display()
cube.rotate_U_counterclockwise()
cube.display()
