
SPLITS = 1024
cache = dict()
for i in range(0,SPLITS,1):
    cache[i] = list()

count = 0
for i in range(1,31,1):
    digit = ''
    if i<10:
        digit = '0'+str(i)
    else:
        digit = str(i)
    filename = '../data/querylog/201204'+digit+'.dat'
    print filename
    fin = open(filename)
    line  = fin.readline()
    while line != '':
        try:
            
            segs = line.strip().split('\t')
            if len(segs)>2:
                userid =segs[1]
                hashmod = userid.__hash__()%SPLITS
                cache[hashmod].append(line)
                count +=1
        except:
            print count,"EXCEPT"
        if count%50000000==0:
            print 'Writing ',count,filename
            for idx in range(0,SPLITS,1):
                fout = open('../data/querylogbyid/'+str(idx)+'.dat','a')
                for item in cache[idx]:
                    fout.write(item)
                fout.close()
                cache[idx] = list()
        line  = fin.readline()

print 'Final Clearing'
for idx in range(0,SPLITS,1):
    fout = open('../data/querylogbyid/'+str(idx)+'.dat','a')
    for item in cache[idx]:
        fout.write(item)
    fout.close()
    cache[idx] = list()