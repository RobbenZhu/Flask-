import smtplib
from email.mime.multipart import MIMEMultipart 
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.application import MIMEApplication
import time
import yagmail
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time
# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# BlockingScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', seconds = 120)#每2min运行1次
scheduler.start()
#发件人邮箱
asender="1144015697@qq.com"
#收件人邮箱
areceiver="dyk2021@mail.ustc.edu.cn"
#抄送人邮箱
acc = '1362536452@qq.com'
#邮件主题
asubject = '你没爸，你没妈，你是唯一的神话,我是你多多爹' 
 
#发件人地址
from_addr = "1144015697@qq.com"
#邮箱密码（授权码）
password="jbmxeggbxcdqhjeh"
 
#邮件设置
msg = MIMEMultipart()
msg['Subject'] = asubject  
msg['to'] = areceiver  
msg['Cc'] = acc 
msg['from'] =  "坤坤"

#邮件正文
body = "你是憨批"
 
#添加邮件正文:
msg.attach(MIMEText(body, 'plain', 'utf-8'))
#设置邮箱服务器地址以及端口
smtp_server ="smtp.qq.com"
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
 
#登陆邮箱
server.login(from_addr, password)
#发送邮件
i=100
while i :
    server.sendmail(from_addr, areceiver.split(',')+acc.split(','), msg.as_string())
    i=i-1
    print("我是大爹")
    time.sleep(120)
#断开服务器链接
server.quit()