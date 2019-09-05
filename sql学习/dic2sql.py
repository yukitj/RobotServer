import pymysql

def dic2sql(rbts_state, sql): #将字典转为字符串
    sf = ''

    for key in rbts_state:
        tup = (key,rbts_state[key])
        sf += (str(tup)+',')
    sf = sf.rstrip(',')

    sql2 = sql % sf
    return sql2
    
if __name__ == '__main__':
    rbts_state = {'192.168.2.2':133, '192.168.2.3':166}
    sql = "insert into YTRBTS (IP,CART_POS) values %s;"

    ret = dic2sql(rbts_state,sql)

    db = pymysql.connect("localhost","root","root","testdb")
    cursor = db.cursor()
    cursor.execute(ret)
    db.commit()
    db.close()