# excelToTxt
This work will let you extract your excel files column distinct data into txt file(100 excels can be one folder). The txt file name will be like ColumnName_CountOfDistinctValues and content will be comma separated values of the column(values will be there from all the excel files for that column). 
variables used
excelPath->Provide excel files directory path
textPath->Provide txt file path where results will be stored

-If you do not want to drop duplicates you can comment below lines of code
df=df.drop_duplicates()
content=set(content)
