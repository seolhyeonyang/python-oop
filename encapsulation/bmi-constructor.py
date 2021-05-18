class Bmi:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

'''
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만
'''

    def gbmi(self):
        bmi = ''
        index = self.weight / self.height ** 2 * 10000
        if index >= 35:
            bmi = '고도비만'
        elif index >= 30:
            bmi = '중(重)도 비만 (2단계 비만)'
        elif index >= 25:
            bmi = '경도 비만 (1단계 비만)'
        elif index >= 23:
            bmi = '과체중'
        elif index >= 18.5:
            bmi = '정상'
        else:
            bmi = '저체중'

        return bmi

    @staticmethod
    def main():
        b = Bmi(int(input('키(cm): ')), int(input('몸무게(kg): ')))
        print(f'비만도: {b.gbmi()}')

Bmi.main()