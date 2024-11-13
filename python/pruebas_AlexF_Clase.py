from datetime import date, time, datetime

dt = datetime.now()
fechaentrega = f"{dt.year}-{dt.month}-{dt.day + 7}"
print(fechaentrega)