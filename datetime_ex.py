import datetime

now = datetime.datetime.now()

#print('Текущая дата и время', str(now).split('.')[0][0:16])
print('Текущая дата и время', now.strftime('%d.%m.%Y %H:%M'))

d1 = datetime.datetime.fromisoformat('2022-02-28')
print('Моя дата: ', d1)
