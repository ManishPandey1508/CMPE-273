import subprocess
import re

# This code is written for window Machine using windows 10 operating
# system. It might work differently on any othe rmachine.

regionsIPData = {'us-east-1 [23.23.255.255]': '23.23.255.255',
                 'us-west-1 [50.18.56.1]': '50.18.56.1',
                 'eu-west-1 [34.248.60.213]': '34.248.60.213',
                 'us-west-2 [35.160.63.253]': '35.160.63.253',
                 'eu-central-1 [35.156.63.252]': '35.156.63.252',
                 'eu-west-2 [52.56.34.0]': '52.56.34.0',
                 'us-gov-west-1 [52.222.9.163]': '52.222.9.163',
                 'ca-central-1 [52.60.50.0]': '52.60.50.0',
                 'us-east-2 [52.14.64.0]': '52.14.64.0',
                 'ap-northeast-1 [13.112.63.251]': '13.112.63.251',
                 'ap-northeast-2 [52.78.63.252]': '52.78.63.252',
                 'ap-southeast-1 [46.51.216.14]': '46.51.216.14',
                 'ap-southeast-2 [13.54.63.252]': '13.54.63.252',
                 'ap-south-1 [35.154.63.252]': '35.154.63.252',
                 'sa-east-1 [52.67.255.254]': '52.67.255.254',
                 }
outputIpLatency = {}


def fetchLatency(value):
    ping = subprocess.Popen(
        ["ping", "-n", "3", value],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    out, error = ping.communicate()
    print(out)
    m = re.search(r'Average = (.*?)ms', out)
    averageLatency = m.group(1)
    outputIpLatency[key] = int(averageLatency)
    return
for key, value in regionsIPData.items():
    fetchLatency(value)

for key, value in sorted(outputIpLatency.iteritems(), key=lambda (k, v): (v, k)):
    print "%s: %s" % (key, value)
