class Stock(object):

    def __init__(self, name, code, per, pbr, divi):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.divi = divi

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, divi):
        self.divi = divi


ss = Stock('삼성전자', '005930', '15.79', '1.33', '2.83')
ss.set_per(12.75)
print(ss.per)

