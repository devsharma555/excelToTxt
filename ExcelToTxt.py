# Run "pip install pandas" to install pandas 

from pandas import read_excel
import os

excelPath = 'C:\\Users\\DELL\\Desktop\\PythonExcel'  # Provide your excel files folder path
textPath = 'C:\\Users\\DELL\\Desktop\\PythonTxt' #Provide your text file store path
column = input('Enter column name') #user provided column name at runtime
column=column.upper()
fileList = os.listdir(excelPath) #list of all the files provided in excelPath
print(fileList)
a=[]
for i in fileList:
    df = read_excel(f'{excelPath}\\{i}')
    df = df[column]
    df=df.drop_duplicates()
    b = df.values.tolist()
    b=b[:-1]
    a.extend(b)
a=set(a)
count=len(a)
print(a)
print(count)
str=''
str=', '.join(a)
file1=open(f'{textPath}\\{column}_{count}.txt','w')
str=str[:-2]
file1.write(str)
file1.close()



