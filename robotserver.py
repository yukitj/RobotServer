import socketserver, time, json,pymysql,smtplib
from email.mime.text import MIMEText
from email.header import Header

rbts_state = {}
state_req = [b'cart_pos\r', b'jnt_pos\r', b'jnt_vel\r', b'jnt_trq\r', b'alarm_info\r', b'state\r', b'robot_running_state\r'] #状态监控指令队列

def  create(): #创建数据库
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

def insert(value): #插入数据库
    db = pymysql.connect("localhost","root","root","testdb")

    cursor = db.cursor()
    #按指令队列存入数据库
    sql = "INSERT INTO YTRBTS(IP,CART_POS,JNT_POS,JNT_VEL,JNT_TRQ,ALARM_INFO,STATE,RUNNING_STATE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql,(value))
        db.commit()
        print('插入数据成功')
    except:
        db.rollback()
        print('插入数据失败')
    db.close()

def stm(key,r):#发送邮件
    timsd=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))#定义时间格式
    sender = "lizhongyuan@chnrobot.cn"#
    revw = "9216641@qq.com"
    zhengwen = '[+]IP is ''{}\n'\
        '[+]state is ''{}\n'\
        '[+]time is {}\n'.format(key,r,timsd)
    msg = MIMEText(zhengwen)
    msg['From']=Header('lizhongyuan@chnrobot.cn')
    msg['To']=Header('9216641@qq.com','utf-8')
    sub="机器人报错邮件"
    msg['subject']=Header(sub,'utf-8')
    try:
        smtp=smtplib.SMTP()
        smtp.connect('smtp.263.net',25)
        smtp.login('lizhongyuan@chnrobot.cn','yukitj6324')
        smtp.sendmail(sender,revw,msg.as_string())
        print('[+]发送出')
    except Exception as g:
        print('[+]发送失败，原因：',g)

class RokaeRbtHandler(socketserver.BaseRequestHandler):

    def handle(self):
        key = self.client_address[0]
        l = len(state_req)
        r = [None] * l
        lst =[]
        conn = True
        if key == '192.168.2.100':
            a = self.request.recv(1024)
            if a == b'get_robots_info':
                self.request.sendall(json.dumps(rbts_state).encode('utf-8'))
            else:
                self.request.sendall(b'{}')
            return
        while conn:
            time.sleep(1)
            for i in range(l):   #取state_req指令队列长度
                try:
                    self.request.sendall(state_req[i])  #逐条发送
                    a = self.request.recv(1024)   #控制柜返回信息
                except ConnectionError:
                    conn = False
                    break
                if not a:
                    conn = False
                    break
                r[i] = a.strip().decode('utf-8')
            if conn:
                rbts_state[key] = r
                #print(rbts_state)
                #插入数据库
                for key,values in rbts_state.items():#迭代key，values
                    lst=[key]+values#将rbts_state重组为列表
                    insert(lst)
                    if r[6]=='false':#出错发送邮件
                        stm(key,r)
                    
            else:
                rbts_state.pop(key)
            
if __name__ == "__main__":
    #create()

    HOST, PORT = "192.168.2.100", 9999

    with socketserver.ThreadingTCPServer((HOST, PORT), RokaeRbtHandler) as server:
        server.serve_forever()

