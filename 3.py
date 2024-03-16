import csv


def search(name, data):
    '''
    поиск монстра по введенному имени
    :param name: имя монстра
    :param data: массив поиска
    :return: харрактеристики монстра
    '''
    for line in data:
        if line[0] == name:
            return line

def main():
    with open('monster_game.txt', encoding='utf8') as file:
        row = file.readline().split('$')
        data = list(csv.reader(file, delimiter='$'))
        print(row)
        print(data)
        name = input()
        while name!='мир':
            mdata = search(name, data)
            if mdata:
                print(f'{mdata[0]}: {mdata[3]}, {mdata[4]}, {mdata[5]}, {mdata[6]}')
            else:
                print('Ого, вам попался новый монстр! БЕГИТЕ!')
            name = input()

if __name__ == '__main__':
    main()

