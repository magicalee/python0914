day_of_week = ('Sunday','Monday')
day_of_week += 'Tuesday',
print day_of_week
print day_of_week[0],day_of_week[2]
print [len(day) for day in day_of_week]
print 'Wednesday'*5
print ('Wednesday',)*5

def split_head(sequence):
    return sequence[0],sequence[1:]
dayOfweek=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
first,remain=split_head(dayOfweek)
print 'first=',first,', and remain=',remain