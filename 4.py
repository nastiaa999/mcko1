import csv

def experience(line):
    '''
    Подсчет опыта
    :param line: данные о монстре
    :return: список с именем монстра и опытом, который можно получить
    '''
    attack, protect, heal, speed = int(line[3]), int(line[4]), int(line[5]), int(line[6])
    if line[1] == 'усиление атаки':
        return [line[0], int(attack*1.5+ protect+heal+speed)]
    if line[1] == 'регенерация':
        return [line[0], int(heal*1.5+protect+attack+speed)]
    if line[1] == 'дополнительный ход':
        return [line[0], int(speed*1.5 +protect+heal+attack)]


def main():
    with open('monster_game.txt', encoding='utf8') as file:
        row = file.readline().split('$')
        data = list(csv.reader(file, delimiter='$'))

        data1 = []
        for line in data:
            data1.append(experience(line))

        c = 0
        for line in data1:
            print(line)
            c+=1
            if c==10: break

if __name__ == '__main__':
    main()
