from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsMusic(object):

    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def scrap(soup):
        s = input('조회할 목록')
        print(f'---------------- {s} RANKING------------------')
        count = 0
        for i in soup.find_all(name='p', attrs=({"class": f'{s}'})):
            count += 1
            print(f'{str(count)} 위')
            print(f'{s}: {i.find("a").text}')

# https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input(' 0:Exit\n 1:Input URL\n 2:Get Ranking\n')

            if menu == '0':
                break

            elif menu == '1':
                bugs.url = input('Input URL')

            elif menu == '2':
                print(f'Input URL is {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                bugs.scrap(soup)

                bugs.scrap(soup)

            else:
                print('Wrong Number')
                continue

BugsMusic.main()