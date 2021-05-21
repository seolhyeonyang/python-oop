'''
이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
'''

class Contacts(object):

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def get_contact(self):
        return f'주소록: 이름 {self.name}, ' \
               f'전화번호 {self.phone}, ' \
               f'이메일 {self.email}, ' \
               f'주소 {self.address}'

    @staticmethod
    def del_elem(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0:종료, 1:추가, 2:출력, 3:수정 4:삭제')
            if menu == '0':
                print('종료')
                break

            elif menu == '1':
                ls.append(Contacts(input('이름'),
                                   input('전화번호'),
                                   input('이메일'),
                                   input('주소')))

            elif menu == '2':
                for i in ls:
                    print(f'출력결과 {i.get_contact()}')

            elif menu == '3':
                name = input('수정할 이름')
                contancts = Contacts(name,
                                     input('수정할 전화번호 '),
                                     input('수정할 이메일 '),
                                     input('수정할 주소'))
                contancts.del_elem(ls, name)
                ls.append(contancts)

            elif menu == '4':
                name = input('삭제할 이름: ')
                contancts = Contacts(name, None, None, None)
                contancts.del_elem(ls, name)

            else:
                print('잘못된 주문입니다.')
                continue

Contacts.main()
