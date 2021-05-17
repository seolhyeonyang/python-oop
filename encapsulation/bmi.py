class Bmi:
    def setbmi(self,hei,wei):
        self.hei = hei
        self.wei = wei

    def div(self):
        return (b.wei / (b.hei*2))*100

if __name__ == '__main__':
    b = Bmi()
    b.setbmi(160,50)
    print(b.div())