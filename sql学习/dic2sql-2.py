import pymysql
def insert(table,data):
    data = {'ip':'123','ip':'456'}
    table = 'users'
    #获取到一个以键且为逗号分割的字符串，返回一个字符串
    keys = ','.join(data.keys())
    values = ','.join(['%s'] *len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)
    #这里的第二个参数传入的要是一个元组
    if cursor.execute(sql, tuple(data.values())):
        print('users')
        db.commit()

db = pymysql.connect('localhost','root','root','testdb')
cursor =db.cursor()
insert("1","2")