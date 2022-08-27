from output import read_data
from input import write_data


def delete (listDel):
    data = read_data()
    newData =[]
    for el in data:
        if not el in listDel:
            newData.append(el)
 # print(newData)
    f = open('phonebook.csv', 'w')
    f.close()
    for line in newData:
        write_data(line,',')