# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pprint import pprint
import csv
import re
#lastname,firstname,surname,organization,position,phone,email
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # читаем адресную книгу в формате CSV в список contacts_list
    result_list = []
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter="\n")
        contacts_list = list(rows)
    #pprint(contacts_list)

    for cont in contacts_list:
        res = re.sub(r"[;,\s']", r" ", str(cont))
        res = re.sub(r"([-!~_0-9a-zA-Z/.]+@[-!~_0-9a-zA-Z/.]+)", r"#\1 ", str(res)) #почта
        res = re.sub(r"(\s)+", r" ", str(res))
        res = re.sub(r"(([А-ЯЁ][а-яё]+[ ])([А-ЯЁ][а-яё]+[ ])([А-ЯЁ][а-яё]+)*)", r"\2#\3#\4, ", str(res))
        res = re.sub(r"( )+", r" ", str(res))
        res = re.sub(r"(,)( [А-ЯЁа-яё]*)", r"#\2,", str(res)) #место работы
        res = re.sub(r"(,)([–a-zА-ЯЁа-яё ]*|$)", r"#\2\1 ", str(res), flags = re.MULTILINE) #должность
        res = re.sub(r"(,)( |#)((8|[/+]7|7)*([/(/)\d -]*))(( )|[#a-zA-Z@0-9]+|!|$)", r"#8\5\1\6", str(res)) #телефон
        res = re.sub(r"(,)((/(| )(доб/. [0-9]+)(/)| ))", r"#\4", str(res)) #добавочный
        res = re.sub(r",", r"#", str(res))
        res = re.split(r"#",res)

        while len(res) < 8:
            res += ' '
        res[0] = re.sub(r"[ /[]",r"",str(res[0]))
        res[1] = re.sub(r" ", r"", str(res[1]))
        res[2] = re.sub(r" ", r"", str(res[2]))
        res[3] = re.sub(r" ", r"", str(res[3]))
        if res[5] in ['8','',' ']:
            res[5] = ''
        elif len(res[5]) > 4:
            res[5] = re.sub(r"[/)|/(]", r"", str(res[5]))
            res[5] = re.sub(r" ", r"", str(res[5]))
            res[5] = re.sub(r"-", r"", str(res[5]))
            res[5] = '+7(' + res[5][1:4] + ')' + res[5][4:7] + '-' + res[5][7:9] + '-' + res[5][9:11]
            if len(res[6]) > 4:
                res[6] = re.sub(r"[/)|/(]", r"", str(res[6]))
                res[6] = re.sub(r" ", r"", str(res[6]))
                res[6] = re.sub(r"-", r"", str(res[6]))
                res[6] = re.sub(r"(доб.)(\d+)(\D)*", r"\2", str(res[6]))
                res[5] += ' доб.' + res[6]
        res[7] = re.sub(r"[ /]]", r"", str(res[7]))
        result_list += [[res[0], res[1], res[2], res[3], res[4], res[5], res[7]]]
    print(result_list)
    delet_ind = []
    for i in range(0, len(result_list)-1):
        for j in range(i+1, len(result_list)):
            if result_list[i][0] == result_list[j][0] and result_list[i][1] == result_list[j][1]:
                for n in range(3,7):
                    if len(result_list[i][n]) < len(result_list[j][n]) and len(result_list[j][n]) > 1:
                        result_list[i][n] = result_list[j][n]
                        delet_ind += [j]
    print(result_list)
    print(delet_ind)
    k = 0
    for i in delet_ind:
        result_list.pop(i - k)
        k += 1
    result_list[0] = ['lastname','firstname','surname','organization','position','phone','email']
    print(result_list)
    # TODO 1: выполните пункты 1-3 ДЗ
    # ваш код

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(result_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
