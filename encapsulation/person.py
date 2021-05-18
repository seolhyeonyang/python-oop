'''
이름, 출생년도, 주소를 입력받아서
회원가입한 사람의 이름, 나이(만), 주소를 출력하시오.
'''

class Person(object):

    def __init__(self,name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def a(self):
        return 2021 - self.age

    @staticmethod
    def main():
        p = Person(input('이름: '), int(input('출생년도: ')), input('주소: '))
        print(f'나이(만): {p.a()}')

Person.main()

