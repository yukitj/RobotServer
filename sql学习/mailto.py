import smtplib,time
from email.mime.text import MIMEText
from email.header import Header

key = '192.168.1.1'
r = ['149.36,252.00', '90.00', '0.00', '4.0000', '', 'MOTOR_ON', 'true']



def stm():
    timsd=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    sender = "lizhongyuan@chnrobot.cn"
    revw = "9216641@qq.com"
    zhengwen = '[+]IP is ''{}\n'\
        '[+]state is ''{}\n'\
        '[+]time is {}\n'.format(key,r,timsd)
    msg = MIMEText(zhengwen)
    msg['From']=Header('lizhongyuan@chnrobot.cn')
    msg['To']=Header('9216641@qq.com','utf-8')
    sub="报错邮件"
    msg['subject']=Header(sub,'utf-8')
    try:
        smtp=smtplib.SMTP()
        smtp.connect('smtp.263.net',25)
        smtp.login('lizhongyuan@chnrobot.cn','yukitj6324')
        smtp.sendmail(sender,revw,msg.as_string())
        print('[+]发送出')
    except Exception as g:
        print('[+]发送失败，原因：',g)

if r[6] == 'true':
    stm()

