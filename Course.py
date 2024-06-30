class Course:

    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.grademap = []

    # adds the student and his grade to the course
    # need to also add the course to the studant object
    def addStudent(self, student, grade):
        self.grademap[student] = grade

    def getStudentGrade(self, student):
        return self.grademap.get(student)

    #returns the average of the course
    def getAverage(self):
        return sum(self.grademap.values()) / len(self.grademap.values())

    #returns the median of the course
    def getMedian(self):
        return sorted(self.grademap.values())[len(self.grademap.values()) // 2]

    #returns the prectenge of falis in this class
    def getFailPrecentage(self):
        return filter(lambda x: x < 60, self.grademap.values()) / len(self.grademap.values())

    #gets int k and returns the k largest grade in the course.
    def getKgrade(self, k):
        return sorted(self.grademap.values())[k]
