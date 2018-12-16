import pyodbc

con = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = 'WIN_81', database='Risa')

def dataset1risa():
    with open("dataset_1.txt") as file:
           firstline = (file.readline())
           isirisa = firstline.split('\t')
           print (isirisa)

           sql = "use Risa create table dataset1(" + isirisa[0] + " INT," + isirisa[1] + " VARCHAR(255)," + isirisa[2] + " VARCHAR(255),Last_Access Datetime)"
           cursor = con.cursor()
           cursor.execute(sql)
           con.commit()
           print('dataset1 ok')

dataset1risa()

def dataset2risa():
    with open("dataset_2.txt") as file:
           firstline = (file.readline())
           isirisa = firstline.split('\t')
           print (isirisa)

           sql = "use Risa create table dataset2("+ isirisa[0] +" INT," + isirisa[1] + " VARCHAR(255)," + isirisa[2] + " VARCHAR(255)," + isirisa[3] + " VARCHAR(255)," + isirisa[4] + " VARCHAR(255),Last_access Datetime,Email VARCHAR(255))"
           cursor = con.cursor()
           cursor.execute(sql)
           con.commit()
           print('dataset2 ok')
dataset2risa()

def dataset3risa():
    with open("dataset_3.txt") as file:
           firstline = (file.readline())
           isirisa = firstline.split('\t')
           print (isirisa)

           sql = "use Risa create table dataset3("+ isirisa[0] +" INT," + isirisa[1] + " VARCHAR(255)," + isirisa[2] + " VARCHAR(255)," + isirisa[3] + " VARCHAR(255)," + isirisa[4] + " VARCHAR(255),Last_access Datetime,Email VARCHAR(255))"
           cursor = con.cursor()
           cursor.execute(sql)
           con.commit()
           print('dataset3 ok')

dataset3risa()