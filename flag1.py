import pyodbc as py
import string
import csv

db_servername='10.0.2.19'
db_database='asset'
db_username='SA'
db_password='Soulsvciot01'

cnxn = py.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + db_servername + ';DATABASE=' + db_database + ';UID=' + db_username + ';PWD=' + db_password)

list2=[]
list3=[]

with open("/home/u_admin/Asset report 1500 electronics (2).csv",'r',encoding="utf-8") as file:
    reader = csv.reader(file)
    header=next(reader)
    for row in reader:
        list2.append(row)
    #print(list2)

for i in list2:
    assets_id=i[1]
    cursor=cnxn.cursor()
    cursor.execute("""INSERT INTO test(asset_id)values(?)""",str(assets_id))

cnxn.commit()
