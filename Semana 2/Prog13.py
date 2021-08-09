#datetime

import datetime

time = datetime.datetime(2021, 8, 8, 23, 14, 10, 10000)
today = datetime.datetime.today()
now = datetime.datetime.now()
utc = datetime.datetime.utcnow()
time_str = 'August 08, 2021'

print(time)
print(today)
print(now)
print(utc)
print(time.strftime('%B %d, %Y'))
print(time.strptime(time_str, '%B %d, %Y'))