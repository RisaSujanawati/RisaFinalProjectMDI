import pyodbc
import dateparser as dp

con = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = 'WIN_81', database='Risa')

def insertdataset1():
        with open("dataset_1.txt") as file:
            firstline = list(file.readlines())

            for a in range(len(firstline)):
                try:
                    if a == 0:
                        print('pass')
                    else:
                        all = list(firstline[a].split('\t'))
                        value = ''
                        for b in range(len(all)):
                            if b == len(all)-1:
                                value = value+",\'"+str(dp.parse(all[b]))[:-7]+ "\'"
                            elif b== 0:
                                value = value+all[b]
                            else:
                                if value == '':
                                    value = value+"\'"+all[b].replace("\n","").replace("'","")+"\'"
                                else:
                                    value = value + ",\'" + all[b].replace("\n","").replace("'","") + "\'"
                        sql = "INSERT INTO [Risa].[dbo].[dataset1] ([No],[Username],[Nama],[Last_Access]) VAlUES(" + value + ")"

                        cursor = con.cursor()
                        cursor.execute(sql)
                        con.commit()
                        print(sql)
                except(pyodbc.DataError):
                    pass
insertdataset1()


def insertdataset2():
    with open("dataset_2.txt") as file:
        firstline = list(file.readlines())

        for a in range(len(firstline)):
            try:
                if a == 0:
                    print('pass')
                else:
                    all = list(firstline[a].split('\t'))
                    value = ''
                    for b in range(len(all)):
                        if b == len(all) - 2:
                            value = value + ",\'" + str(dp.parse(all[b])) + "\'"
                        elif b == 0:
                            value = value + all[b]
                        else:
                            if value == '':
                                value = value + "\'" + all[b].replace("\n", "").replace("'", "") + "\'"
                            else:
                                value = value + ",\'" + all[b].replace("\n", "").replace("'", "") + "\'"
                    sql = "INSERT INTO [Risa].[dbo].[dataset2]([No],[Fakultas],[Jurusan],[Matakuliah],[Dosen],[Last_access],[Email]) VAlUES(" + value + ")"
                    
                    cursor = con.cursor()
                    cursor.execute(sql)
                    con.commit()
                    print(sql)
            except(pyodbc.DataError):
                pass
insertdataset2()


def insertdataset3():
    with open("dataset_3.txt") as file:
        firstline = list(file.readlines())

        for a in range(len(firstline)):
            try:
                if a == 0:
                    print('pass')
                else:
                    all = list(firstline[a].split('\t'))
                    value = ''
                    for b in range(len(all)):
                        if b == len(all) - 2:
                            value = value + ",\'" + str(dp.parse(all[b])) + "\'"
                        elif b == 0:
                            value = value + all[b]
                        else:
                            if value == '':
                                value = value + "\'" + all[b].replace("\n", "").replace("'", "") + "\'"
                            else:
                                value = value + ",\'" + all[b].replace("\n", "").replace("'", "") + "\'"
                    sql = "INSERT INTO [Risa].[dbo].[dataset3]([No],[Fakultas],[Jurusan],[Matakuliah],[Mahasiswa],[Last_access],[Email]) VAlUES(" + value + ")"

                    cursor = con.cursor()
                    cursor.execute(sql)
                    con.commit()
                    print(sql)
            except(pyodbc.DataError):
                pass
insertdataset3()