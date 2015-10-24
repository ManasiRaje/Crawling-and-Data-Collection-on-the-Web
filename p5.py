import csv
#import pandas

#colnames = ['hashtag', 'from', 'to', 'NoR', 'TFN']
#data = pandas.read_csv('C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\Super_Bowl_csv.csv', names=colnames)
#no_of_results = list(data.NoR)

list_super_bowl = []
with open('C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\Super_Bowl_csv.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        list_super_bowl.append(row[3])
list_super_bowl = map(int, list_super_bowl)

list_nfl = []
with open('C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\NFL_csv.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        list_nfl.append(row[3])     
list_nfl = map(int, list_nfl)

#step = 10 => sample at every t, t(i+1) - t(i) = 10 min = 600 sec
sampling_interval = 10
newlist_super_bowl = []
for i in range(10,len(list_super_bowl)+1, sampling_interval):
    newlist_super_bowl.append(float(sum(list_super_bowl[0:i]))/(i*60))

newlist_nfl = []
for i in range(10,len(list_nfl)+1, sampling_interval):
    start = i
    end = i + 10
    newlist_nfl.append(float(sum(list_nfl[0:i]))/(i*60))




