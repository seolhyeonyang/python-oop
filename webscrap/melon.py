from bs4 import BeautifulSoup
import requests

class Melon(object):

    url = ''

    def __str__(self):
        return self.url

    '''
    @staticmethod
    def scrap(soup):
        print('---------TITLE RANKING----------')
        count = 0
        for i in soup.find_all(name='div', attrs=({'class':'ellipsis rank01'})):
            count += 1
            print(f'{str(count)} 위')
            print(f'TITLE: {i.find("a").text}')
    '''


# https://www.melon.com/chart/index.htm
    @staticmethod
    def main():
        melon = Melon()
        while 1:
            m = input('0:Exit\n1:Input URL\n2:Get RANKING\n')

            if m == '0':
                break

            elif m == '1':
                melon.url = input('Input URL')

            elif m == '2':
                print(f'Input URL is {melon}')
                header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
                res = requests.get(melon, headers = header).text
                soup = BeautifulSoup(res, 'lxml')

                print('---------ARTIST RANKING----------')
                count = 0
                for i in soup.find_all(name='div', attrs=({'class': 'ellipsis rank02'})):
                    count += 1
                    print(f'{str(count)} 위')
                    print(f'ARTIST: {i.find("a").text}')

                print('---------TITLE RANKING----------')
                count = 0
                for i in soup.find_all(name='div', attrs=({'class': 'ellipsis rank01'})):
                    count += 1
                    print(f'{str(count)} 위')
                    print(f'TITLE: {i.find("a").text}')

            else:
                continue

Melon.main()