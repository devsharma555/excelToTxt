# Run "pip install pandas" to install pandas 

from pandas import read_excel
import os

excelPath = 'C:\\Users\\DELL\\Desktop\\PythonExcel'  # Provide your excel files folder path
textPath = 'C:\\Users\\DELL\\Desktop\\PythonTxt' #Provide your text file store path
column = input('Enter column name') #user provided column name at runtime
column=column.upper()

fileList = os.listdir(excelPath) #list of all the files provided in excelPath
print(fileList)
content=[]

for i in fileList:
    df = read_excel(f'{excelPath}\\{i}')
    df = df[column]
    df=df.drop_duplicates()
    excelColumnValues = df.values.tolist()
    excelColumnValues=excelColumnValues[:-1]
    content.extend(excelColumnValues)

content=set(content)
count=len(content)
print(content)
print(count)
finalContent=''
finalContent=', '.join(map(str,content))   #map(str,content) used To handle int, float or any other datatype if not string

file1=open(f'{textPath}\\{column}_{count}.txt','w')
finalContent=finalContent[:-2]
file1.write(finalContent)

file1.close()




