sales = {'iphone7':1000,'iphone7s':1500,'iphone8':3500,'iphone8s':5000}
print sales['iphone7s'],sales['iphone8']
print sales.get('iphoneX'),sales.get('iphone8')
print 'iphone7' in sales , 'iphoneX' in sales
print [key+'/'+str(sales[key]) for key in sales.keys()]
total=0
for value in sales.values():
    total += value
    print value
print total
for item in sales.items():
    print type(item),len(item)
    print item[0],item[1]

sales['iphoneX']=2500
print [key+':'+str(value) for key,value in sales.items()]
sales.update({'iphone7':500,'iphone7s':1300,'ipad':2000})
total = 0
for value in sales.values():
    total += value
    print value
print total