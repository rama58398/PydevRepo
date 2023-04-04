with open("C:/Users/rkraj/Documents/change.txt", "r") as filehandler:
    filecontent = filehandler.readlines()
    d=dict()
    for line in filecontent:
        line=line.rstrip()
        wds=line.split()
        for w in wds:
            d[w]=d.get(w,0)+1
   # print(d)
    largest=0
    theword=None

    for k,v in d.items():
        #print(k,v)
        if v>largest:
            largest=v
    print('"Done"',k, largest)




