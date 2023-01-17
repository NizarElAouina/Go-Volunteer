import sqlite3

class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.c=self.con.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS datas(pid INTEGER PRIMARY KEY,name TEXT ,cin TEXT ,Tel TEXT ,address TEXT ,typedonation TEXT , description TEXT )")
        self.con.commit()

    def insert(self,name,cin,telephone,address,typedonation,description):
        sql="""
            insert into datas values(NULL,?,?,?,?,?,?)
        """
        self.c.execute(sql,(name,cin,telephone,address,typedonation,description))
        self.con.commit()

    def fetch_record(self):
        self.c.execute("SELECT * FROM datas")
        data = self.c.fetchall()
        return data

    def update_record(self,name,cin,telephone,address,typedonation,description,pid):
        sql="""
            update datas set name=?,cin=?,telephone=?,address=?,typedonation=?,description=? where pid=?
        """
        self.c.execute(sql,(name,cin,telephone,address,typedonation,description,pid))
        self.con.commit()

    def remove_record(self,pid):
        sql="delete from datas where pid=?"
        self.c.execute(sql,(pid,))
        self.con.commit()

