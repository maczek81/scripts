import sys
import os
from sets import Set

def main():
    useragents = Set()
    if len(sys.argv) > 1:
        try:
            logfile = open(sys.argv[1], "r")
        except:
            sys.exit("Nie ma takiego pliku")
        #logfile = open(sys.argv[1],'rU')
    else:
        print "Podaj nazwe pliku"
        return
    for line in logfile:
        #print line.split('"')[5]
        useragents.add(line.split('"')[5])
    logfile.close()
    for useragent in useragents:
        print useragent
    print "-------------------------------"
    print "Liczba unikalnych User-agent'ow: " , len(useragents)
if __name__ == '__main__':
    main()
