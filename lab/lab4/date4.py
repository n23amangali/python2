from datetime import datetime
x=input()
y=input()

date_format = '%Y-%m-%d %H:%M:%S'
x=datetime.strptime(x,date_format)
y=datetime.strptime(y,date_format)
z=(x-y).total_seconds()
print({z})