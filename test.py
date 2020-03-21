import datetime as d

delta = [3,10,40]
start = []
end = []

for i in range(3):
    date = d.datetime.now().replace(microsecond=0) + d.timedelta(delta[i])
    start.append(date.isoformat())
    print(start[i])

    date = date + d.timedelta(hours=1)
    end.append(date.isoformat())
    print(end[i])


