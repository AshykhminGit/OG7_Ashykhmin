string = 'Денис даёт нам классные задачки, которые помогут нам найти лучшую работу'
count ={}
for  s in string:
    count [s] = count.get(s, 0) +1
    print (count)