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
        cursor.execute(sql,(values))#插入列表
        db.commit()
        print('插入成功')
    except:
        db.rollback()
        print('插入失败')
    db.close()

if __name__ == "__main__":

    create()

    #item = {'ip':['1','2,4','3','4','no','on','yes']}
    item ={'192.168.2.160': ['15.54,399.85,94.95,-134.85,-0.06,-90.00,-0.27,0.65,-0.65,0.27', '29.73,-12.88,-153.69,50.02,52.03,38.99', '14.96,-20.30,0.65,9.09,6.72,17.10', '82.0000,36.0000,-177.0000,132.0000,159.0000,125.0000', '', 'MOTOR_ON', 'true'], '192.168.2.2': ['-185.97,479.13,-91.13,-135.39,-0.06,-89.86,-0.27,0.66,-0.65,0.27', '42.67,-53.45,-106.04,35.75,58.87,52.16', '-1.74,-2.33,5.97,-2.91,-0.92,-1.74', '-66.0000,262.0000,-207.0000,-7.0000,-72.0000,-99.0000', '', 'MOTOR_ON', 'true']}

    for key,values in item.items():
        #print(key)
        values.insert(0,key) #insert key to values top
    
        #print(values)
        insert(values)
