import os
import csv
from sklearn.cross_validation import train_test_split
import pandas as pd


def split_combine():
    for a in pd.read_csv('Data/Normalised-Data/met_normalised_combine.csv', chunksize=1200):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()

    mylist_train, mylist_test = train_test_split(
        mylist, test_size=0.2)



    if not os.path.exists("../Data/Train"):
        os.makedirs("../Data/Train")
    if not os.path.exists("../Data/Test"):
        os.makedirs("../Data/Test")

    with open('../Data/Train/Train_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(mylist_train)

    with open('../Data/Test/Test_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(mylist_test)


def split(year):
    mylist = []
    if year == 2013:
        cs = 343
    elif year == 2014:
        cs = 346
    elif year == 2015:
        cs = 349
    else:
        cs = 59

    for a in pd.read_csv('../Data/Normalised-Data/met_normalised_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()

    mylist_train, mylist_test = train_test_split(
        mylist, test_size=0.3)

    if not os.path.exists("../Data/Train"):
        os.makedirs("../Data/Train")
    if not os.path.exists("../Data/Test"):
        os.makedirs("../Data/Test")

    with open('../Data/Train/Train_' + str(year) + '.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(mylist_train)

    with open('../Data/Test/Test_' + str(year) + '.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(mylist_test)


def combine_train(year, cs):
    for a in pd.read_csv('Train/Train_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
    mylist = df.values.tolist()
    return mylist


def combine_test(year, cs):
    for a in pd.read_csv('Test/Test_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
    mylist = df.values.tolist()
    return mylist


if __name__ == "__main__":
    split_combine()


