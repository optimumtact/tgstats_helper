import csv
from collections import defaultdict
from datetime import datetime

mappings = defaultdict(dict)
dates = list()
port_mappings = {"1337": "sybil", "2337":"basil", "3337":"terry", "1447":"manuel", "4337":"eu hall", "4447":"us hall"}
with open('daily.tsv') as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  #skip header line
  next(reader)
  for row in reader:
    date = "{2}-{1:02d}-{0:02d}".format(int(row[0]), int(row[1]), row[2])
    if date not in dates:
      dates.append(date)
    server_port = row[4]
    if server_port not in port_mappings:
      print("Unexpected server port {0}, skipping".format(server_port))
      continue
    server = port_mappings[server_port]
    mappings[date][server] = row[3]

dates.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
servers = list(port_mappings.values())
print(servers)
with open('daily-processed.csv', 'w') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  csvwriter.writerow(['date'] + servers)
  for date in dates:
    data = mappings[date]
    final = list()
    final.append(date)
    for server in servers:
      if server in data:
        final.append(data[server])
      else:
        final.append(0)
    csvwriter.writerow(final)
