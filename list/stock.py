class Stock(object):

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def to_stirng(self):
        return f'종목명: {self.name}, 종목코드: {self.code}'

    @staticmethod
    def del_element(ls, code):
        for i, j in enumerate(ls):
            if j.code == code:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0:종료, 1:입력, 2:출력, 3:수정, 4:삭제')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock(input('종목명:'), input('종목코드')))
            elif menu == '2':
                for i in ls:
                    print(i.to_stirng())
            elif menu == '3':
                code = input('종목코드')
                stock = Stock(input('수정할 종목명:'), code)
                stock.del_element(ls, code)
                ls.append(stock)
            elif menu =='4':
                stock = Stock(None, input('종목코드'))
                stock.del_element(ls, stock.code)
            else:
                print('잘못입력 했습니다.')
                continue

Stock.main()


























