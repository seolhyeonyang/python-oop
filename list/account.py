import random

class Account(object):

    def __init__(self, name, money):
        self.bank_name = 'sc은행'
        self.name = name
        self.number = self.get_number()
        self.money = money

    def get_number(self):
        r = random.randint(1,9)
        return f'{r}{r}{r}-{r}{r}-{r}{r}{r}{r}{r}{r}'

    def get_account(self):
        return f'은행: {self.bank_name}, 예금주: {self.name}, 계좌번호: {self.number}, 잔액: {self.money} '

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0:종료, 1:입력, 2:출력, 3:삭제 ')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(input('예금주 '),input('잔액 ')))
            elif menu == '2':
                for i in ls:
                    print(i.get_account())
            elif menu == '3':
                del_name = input('삭제할 이름: ')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
            else:
                print('잘못입력 되었습니다.')
                continue


Account.main()




