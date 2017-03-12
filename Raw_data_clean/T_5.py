import pandas as pd
import collections
import numpy as np
import os,sys,time


class ReadData():

    def __init__(self):
        self.name_list = ['Commodity', 'Currency', 'Economic_Indicator', 'Equity', 'Index','Precious_Metal']
        self.location = '../data'
        self.data_pack = collections.defaultdict()
        self.read_data()
        self.ticker_name = []
        self.read_ticker()


    def read_ticker(self):
        for i in self.name_list:
            print(i,'master')
            dummy = pd.read_csv(self.location + '/' + str(i) + '_Master' +  '.csv')
            self.ticker_name.append(list(dummy.Ticker))

    def read_data(self):
        for i in self.name_list:
            print(i)
            self.data_pack[i] = pd.read_csv(self.location + '/' + str(i) + '_mod' +  '.csv')

    def get_data(self):
        return self.data_pack

    def get_name_list(self):
        return self.name_list

    def get_ticker_name(self):
        return self.ticker_name


def main():
    data = ReadData()
    name_list = data.get_name_list()
    data_pack = data.get_data()
    ticker_name = data.get_ticker_name()

    count = 0
    for i in range(1):
        for j in range(len(ticker_name[i])):
            if count == 0:
                df_a = data_pack[name_list[i]].loc[data_pack[name_list[i]]['Ticker'] == ticker_name[i][j]]
                df_a = df_a[['Date','Close']]
                df_a.columns = ['Date',ticker_name[i][j]]
                merged = df_a
            else:
                df_a = data_pack[name_list[i]].loc[data_pack[name_list[i]]['Ticker'] == ticker_name[i][j]]
                df_a = df_a[['Date','Close']]
                df_a.columns = ['Date',ticker_name[i][j]]
                merged = pd.merge(merged,df_a, on='Date', how='outer')
            count += 1
    print(merged)



if __name__ == '__main__':
    main()
