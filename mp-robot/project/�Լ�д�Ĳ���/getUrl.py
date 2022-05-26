f = open('test.html',encoding ='utf8')
f2 = open('res.txt','a+')
for line in f:
    if '"full": "https:' in line:
        while 'u002F' in line:
            line = line.replace('u002F','')
        while " " in line:
            line = line.replace(" ", "")
        # print(line)
        line = line.replace('"full":"https:','https:').replace('",','')
        if 'https:' in line:
            f2.write(line)
            # f2.write('\n')
f2.close()



        # break