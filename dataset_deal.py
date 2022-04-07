from openpyxl import load_workbook
import pandas as pd
import numpy
wb=load_workbook('Data_dictionary.xlsx')
sheet=wb.get_sheet_by_name('Sheet1')

dic_all={}
i=0
for row in sheet.rows:
    dic = {}
    for cell in row:
        tmp=cell.value
        if '=' in str(tmp):
            sec_a,sec_b = tmp.split("=")
            dic[sec_a]=sec_b
    dic_all[i]=dic
    i=i+1
#print(dic_all)

j=0
result={}
newlog = "newx.csv"
l = open(newlog,'w')
for line in open('NGS.csv'):
    j=j+1
    if "HAND" in line:
        #result[0] = line
        l.write(line)
        continue

    else:
        arr=line.split(",")
        arr[len(arr)-1]=arr[len(arr)-1][:-1]

        for k in range(1,len(arr)):
            tmp=dic_all[k-1]
            if arr[k] in tmp:
                arr[k]=tmp[arr[k]]
        str=','.join(arr)
        l.write(str)
        l.write('\n')


#numpy.savetxt('new.csv',result,delimiter=',',fmt='%s')
print(result)
