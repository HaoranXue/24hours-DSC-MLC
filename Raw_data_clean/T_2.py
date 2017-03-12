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
        print('\r' + str(i) + '/' + str(len(name_list)),end='')
        data_pack[name_list[i]]['Date'] = pd.to_datetime(data_pack[name_list[i]].Date)
        data_pack[name_list[i]]['Date'] = data_pack[name_list[i]]['Date'].dt.strftime('%Y%m%d')

        try:
            new_data_frame = data_pack[name_list[i]][['Date','Close']]
        except:
            new_data_frame = data_pack[name_list[i]][['Date','Value']]

        new_data_frame.to_csv('../data/' + name_list[i] + '_mod'+'.csv',index=False)

    for i in range(len(name_list)):
        print(i)
        print(data_pack[name_list[i]].Date[0])


if __name__ == '__main__':
    main()
