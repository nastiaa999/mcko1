import csv


def power(line):
    '''
    Функция, подсчитывающая мощность силы монстра
    :param line: данные о монстре
    :return: массив с именем монстра, его возможностью и мощностью силы
    '''
    if line[1] == 'регенерация':
        return [line[0], line[1], int(line[5]) * int(line[2]) / 100]
    if line[1] == 'дополнительный ход':
        return [line[0], line[1], sum(map(int, line[3:7])) * int(line[2])/100]
    if line[1] == 'усиление атаки':
        return [line[0], line[1], int(line[3]) * (int(line[2]) / 100)]


def main():
    '''
    Подсчет мощности силы монстров
    :return: мощность силы первых пяти монстров
    '''
    with open('monster_game.txt', encoding='utf8') as file:
        row = file.readline().split('$')
        data = list(csv.reader(file, delimiter='$'))
        data1 = []
    for line in data:
        data1.append(power(line))
    c = 1
    for line in data1:
        print(line[2])
        c+=1
        if c == 5: break


if __name__ == '__main__':
    main()