import pymysql

def  create():
    db = pymysql.connect("localhost","root","root","testdb")#连接数据库

    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS YTRBTS")

    sql = """create table YTRBTS (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        IP CHAR(30),
        CART_POS CHAR(150),
        JNT_POS CHAR(150),
        JNT_VEL CHAR(150),
        JNT_TRQ CHAR(150),
        ALARM_INFO CHAR(50),
        STATE CHAR(50),
        RUNNING_STATE CHAR(50)
    )"""

    cursor.execute(sql)
    db.close()

def insert(value):
    db = pymysql.connect("localhost","root","root","testdb")

    cursor = db.cursor()
    sql = "INSERT INTO YTRBTS(IP,CART_POS,JNT_POS,JNT_VEL,JNT_TRQ,ALARM_INFO,STATE,RUNNING_STATE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql,(item))
        db.commit()
        print('插入成功')
    except:
        db.rollback()
        print('插入失败')
    db.close()

create()

item = ['192','1','2','3','4','no','on','yes']
for i in item:
    print(i)
    insert(i)
