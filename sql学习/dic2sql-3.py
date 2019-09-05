import pymysql
def insert2(table,data):
    db = pymysql.connect('localhost','root','root','testdb')
    cursor =db.cursor()

    data = {'ip':'123','state':'456'}
    cols = ",".join('`{}`'.format(k) for k in data.keys())
    print(cols)

    val_cols = ','.join('%({})s'.format(k) for k in data.keys())
    print(val_cols)

    sql = "insert into users(%s) values(%s)"
    res_sql = sql % (cols, val_cols)
    print(res_sql)

    cursor.execute(res_sql, data)
    db.commit()

    a = [{'state':'789','ip':'666'}]
    cursor.executemany(res_sql,a)
    db.commit()

insert2("1","2")