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

    # for i in ticker_name:
    #     print(i)

    # for i in range(len(name_list)):
    # for tickers in ticker_name[0]:
    #     print(data_pack[name_list[0]].loc[data_pack[name_list[0]]['Ticker'] == tickers])
    df_a = data_pack[name_list[0]].loc[data_pack[name_list[0]]['Ticker'] == ticker_name[0][0]]
    df_a = df_a[['Date','Close']]
    df_a.columns = ['Date',ticker_name[0][0]]
    # print(df_a)
    df_b = data_pack[name_list[0]].loc[data_pack[name_list[0]]['Ticker'] == ticker_name[0][1]]
    df_b = df_b[['Date','Close']]
    df_b.columns = ['Date',ticker_name[0][1]]

    print(pd.merge(df_a, df_b, on='Date', how='outer'))


if __name__ == '__main__':
    main()
