#coding=UTF-8
print '%-10s====' % '0123456789'
print '%-10s====' % '0123456789'*2
print '%-10s====' % '0123'
print '%*s====' % ((-10),'0123')
print '{:<{}s}====' .format ('0123',10)
print '{:>{}s}====' .format ('0123',10)
print '{:<10s}====' .format ('測試')
print u'{:<10s}====' .format (u'測試')
print '{:_^10s}====' .format ('測試')
print '{:$>10s}====' .format ('測試')
print '%.6s'%('這是一個中文的字串，非常厲害')
print u'%.6s'%(u'這是一個中文的字串，非常厲害')
print '{:.{}}'.format('這是一個中文的字串，非常厲害',9)
print u'{:.{}}'.format(u'這是一個中文的字串，非常厲害',9)