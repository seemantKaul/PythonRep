import pandas as pd
import cx_Oracle
import datetime
import calendar
import matplotlib.pyplot as plt


def get_monday(date):
    dt = datetime.datetime(int(date[-4:]),int(date[3:5]),int(date[:2]))
    weekday = datetime.datetime.strptime(date,'%d-%m-%Y').weekday()
    mon = 1
    diff = weekday - mon +1
    days_to_add = 7-diff
#     print(days_to_add)
    return (dt + datetime.timedelta(days=days_to_add)).strftime('%d-%m-%Y')


ip = 'drgldpr.cym6nspxwxod.us-east-1.rds.amazonaws.com'
port = 1521
sid = 'drgldpr'
sql = "select * from PRICINGCYCLEPRICES"
dsn_tns = cx_Oracle.makedsn(ip, port,sid)
conn = cx_Oracle.connect('qc_es1', 'qc_es1$#', dsn_tns)
data = pd.read_sql(sql,conn)

data = pd.read_csv('PRICINGCYCLEPRICES.txt')
list_cycle = list(data['CYCLEID'])
chars = [f"{ch[0]}-{ch[-2:]}" for ch in list_cycle]
data['Frequency']=chars


list_mondays = [get_monday(date) for date in list(data['Date'])]
data['next_monday'] = list_mondays