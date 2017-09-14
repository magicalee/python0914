dayOfweek=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
lenthArray = []
for day in dayOfweek:
    lenthArray.append(len(day))
print lenthArray

print[day+' has length='+str(len(day)) for day in dayOfweek]
sun,mon,tue,wed,thr,fri,sat = dayOfweek
print sun,fri,sat
print "mydata=",tue,wed,thr

number_list=[3,1,4,1,59,23,46,37,51,200]
over30andsorted = sorted(i for i in number_list if i > 30)
print over30andsorted
under40andsorted = sorted((i for i in number_list if i < 40),reverse=True)
print under40andsorted