class Stock(object):

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_stock(self):
        return f'종목명: {self.name}, 종목코드 {self.code}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0:종료, 1:입력, 2:출력, 3:삭제')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock(input('종목명:'), input('종목코드')))
            elif menu == '2':
                for i in ls:
                    print(f'결과: {i.get_stock()}')
            elif menu =='3':
                del_name = input('삭제할 종목')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
            else:
                print('잘못입력 했습니다.')
                continue

Stock.main()


























