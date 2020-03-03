class students:
    def __init__(self,name1,age1, class_):#class
        self.name = name1
        self.age = age1
        self.class_ = "student"


    def avg(self,score1,score2,score3):#method
        result = (score1 + score2 +score3)/3
        return result

course = students("maths","21","year2")

print(" your results" ,course.avg(100, 100, 100))

