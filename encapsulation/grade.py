class Grade:
    def setgrade(self,kor,math,eng):
        self.kor = kor
        self.math = math
        self.eng = eng

    def sum(self):
        return g.kor + g.math + g.eng

    def avg(self):
        return self.sum() / 3

if __name__ == '__main__':
    g = Grade()
    g.setgrade(70,30,40)
    print(g.sum())
    print(g.avg())

