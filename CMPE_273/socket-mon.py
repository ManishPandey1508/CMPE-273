#$ python pip install --upgrade pyformat
#$ python pip install psutil
# python -m pip install pandas

import psutil
import pyformat
import pandas as pd


print'{:{align}{width}} {:{align}{width}} {:{align}{width}} {:{align}{width}} '.format("PID", "LADDR", "RADDR", "STATUS", align='^', width='20')
d = pd.DataFrame()
for conn in psutil.net_connections(kind='tcp'):
    laddr = ""
    raddr = ""
    dictExample = {}
    if(conn.raddr and conn.laddr):
        temp = pd.DataFrame(
            {'PID': conn.pid, 'LADDR': conn.laddr, 'RADDR': conn.raddr, 'STATUS': conn.status})
        d = pd.concat([d, temp])


grouped = d.groupby('PID')

for i in range(0, len(d)):
    print'{:{align}{width}} {:{align}{width}} {:{align}{width}}{:{align}{width}} '.format(d.iloc[i]['PID'], d.iloc[i]['LADDR'], d.iloc[i]['RADDR'], d.iloc[i]['STATUS'], align='^', width='20')
