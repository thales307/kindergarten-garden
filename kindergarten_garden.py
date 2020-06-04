students = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry')
    
PLANTS = {
    
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets'
}

class Garden:
    def __init__(self, diagram, students=students):
        self.diagram = diagram
        self.students = {student: [] for student in sorted(students)}
        self.garden()

    def garden(self):
        rows = self.diagram.split('\n')
        for i, student in enumerate(self.students):
            self.students[student].extend(rows[0][i * 2:i * 2 + 2])
            self.students[student].extend(rows[1][i * 2:i * 2 + 2])
    
    def plants(self, student):
        return list(map(lambda x: PLANTS[x], self.students[student]))