import pandas

def main():
    location = '../data'

    df = pandas.read_csv(location + '/' + 'merged_8.csv')

    print(df)
    df = df.sort_values(by='Date', ascending=[True])
    print(df)
    df.to_csv('../data/' + 'merged_9.csv', index=False)

if __name_ ==  "__main__":
    main()