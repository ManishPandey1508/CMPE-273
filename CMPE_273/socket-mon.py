#$ python pip install --upgrade pyformat
#$ python pip install psutil
# python -m pip install pandas

import psutil
import pyformat
import pandas as pd
import subprocess
import BaseHTTPServer
import sys


d = pd.DataFrame()
for conn in psutil.net_connections(kind='tcp'):
    laddr = ""
    raddr = ""
    dictExample = {}
    if(conn.raddr and conn.laddr):
        temp = pd.DataFrame(
            {'PID': int(conn.pid), 'LADDR': conn.laddr, 'RADDR': conn.raddr, 'STATUS': conn.status})
        d = pd.concat([d, temp])
d['freq'] = d.groupby('PID')['PID'].transform('count')
d = d.sort_values(by=["freq", "PID"], ascending=[False, False])
header = ["PID", "LADDR", "RADDR", "STATUS"]
print d.to_csv(sys.stdout, columns=header, sep=",", index=False)


# print d.columns
# print'{:{align}{width}} {:{align}{width}} {:{align}{width}}
# {:{align}{width}} '.format("PID", "LADDR", "RADDR", "STATUS", align='^',
# width='30')
# for i in range(0, len(d)):
#   print'{:{align}{width}} {:{align}{width}} {:{align}{width}}{:{align}{width}} '.format(d.iloc[i]['PID'], d.iloc[i]['LADDR'], d.iloc[i]['RADDR'], d.iloc[i]['STATUS'], align='^', width='30')
#
