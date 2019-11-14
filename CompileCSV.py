import os
import glob
import pandas as pd
import csv
print('Please paste the filepath containing the .csv files');
filepath = input();

os.chdir(filepath)

extension = 'csv'

all_filenames = [i for i in glob.glob('*.{}'.format(extension))];

#print (all_filenames)

NumFiles = len(all_filenames)-1


Datas = []
i = 1;
while i <= NumFiles: 
    f = open(all_filenames[i])
    contents = f.read()
    Data = contents.splitlines()
    NewData = str(Data).split(', ')
    Datas.append(NewData)
    FileStr = pd.DataFrame(Datas)
    i = i + 1;
#print(FileStr)

contentsCSV = FileStr.to_csv('FileData.csv', index_label=False, encoding = 'utf-8-sig')



