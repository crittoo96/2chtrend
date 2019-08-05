import re
import requests

def create_wget_list():
    with open('kakolog0000.html', 'r') as f:
        file = f.read()
        print(file)

        finds = re.findall(r'kako\d+.html', file)
        dats = re.findall(r'\d+.dat',file)
        print(list(set(finds)))
        print(list(set(dats)))

        with open('wget_list.txt', 'w+') as wgetfile:
            for find in list(set(finds)):
                wgetfile.write('https://swallow.5ch.net/livejupiter/kako/' + find + '\n')

        for dat in list(set(dats)):
            print('https://swallow.5ch.net/test/read.cgi/livejupiter/1564211758/' + dat[:-4])

def create_dat_list():
    with open('wget_list.txt') as f:
        line = f.readline()

        while line:
            try:
                r = requests.get(line)
                print(r.text)
            except requests.exceptions.RequestException as err:
                print(err)

            print(line)
            line = f.readline()
        f.close()

create_wget_list()