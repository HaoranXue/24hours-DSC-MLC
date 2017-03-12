import pandas as pd
import collections
import numpy as np
import os,sys,time


class ReadData():

    def __init__(self):
        self.name_list = ['Precious_Metal', 'Commodity', 'Currency', 'Economic_Indicator', 'Equity', 'Index']
        self.location = '../data'
        self.data_pack = collections.defaultdict()
        self.read_data()

    def read_data(self):
        for i in self.name_list:
            print(i)
            self.data_pack[i] = pd.read_csv(self.location + '/' + str(i) + '.csv')

    def get_data(self):
        return self.data_pack

    def get_name_list(self):
        return self.name_list


def main():
    data = ReadData()
    name_list = data.get_name_list()
    data_pack = data.get_data()

    for i in range(len(name_list)):
        for j in range(len(data_pack[name_list[i]].Date)):
            if j % 200 == 0:
                print('\r' + str(i) + '/' + str(len(name_list)) + '\t' + str(j) + '/' + str(len(data_pack[name_list[i]].Date)),  end='')
            if data_pack[name_list[i]].Date[j][4] == '-':
                data_pack[name_list[i]].Date[j] = data_pack[name_list[i]].Date[j][-2:] + '/' + \
                                                  data_pack[name_list[i]].Date[j][5:7] + '/' + \
                                                  data_pack[name_list[i]].Date[j][0:4]
                # print(data_pack[name_list[i]].Date[j])

        data_pack[name_list[i]].to_csv('../data/' + name_list[i] + '_mod'+'.csv',index=False)

    for i in range(len(name_list)):
        print(data_pack[name_list[i]].Date)


if __name__ == '__main__':
    main()
