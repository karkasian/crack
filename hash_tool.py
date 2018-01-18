import hashlib
import os
import time
import sys
import base64
print """
#########################################
         in the name of allah      
             Hash Tools                  
               author:                   
           MOHAMMAD8500        
      version: 1.0(for windows)  
#########################################

"""
time.sleep(3)
def hashencryptemd5(hashs):
                print "\n"+hashlib.md5(hashs).hexdigest()+"\n"
                time.sleep(10)
                menu()
def hashencryptemdsh1(hashs):
                print "\n"+hashlib.sha1(hashs).hexdigest()+"\n"
                time.sleep(10)
                menu()
def hashencryptesha224(hashs):
                print "\n"+hashlib.sha1(hashs).hexdigest()+"\n"
                time.sleep(10)
                menu()
def hashencryptesha256(hashs):
                print "\n"+hashlib.sha256(hashs).hexdigest()+"\n"
                time.sleep(10)
                menu()
def hashencryptesha384(hashs):
                print "\n"+hashlib.sha384(hashs).hexdigest()+"\n"
                time.sleep(10)
                menu()
def hashencryptesha512(hashs):
                print "\n"+hashlib.sha512(hashs).hexdigest()+"\n"
                time.sleep(10)
                menu()
def hashencryptebase64(hashs):
                print "\n"+str(base64.b64encode(hashs))+"\n"
                time.sleep(10)
                menu()
def hashcrack(hashs2,passwordfile):
                                print "\nLoading Passwords..."
                                try:
                                                 fo = open(passwordfile,"r")
                                                 fr = fo.readlines()
                                except (IOError,UnboundLocalError):
                                                print "Cant read file. Plese check file path \n"
                                os.system('cls')
                                n = 0
                                y = 1
                                print "Cracking ! Plese Wait ...\n"
                                for password in fr:
                                                if hashs2 == hashlib.md5(password.replace('\n','')).hexdigest():
                                                                os.system('cls')
                                                                print " Hash Finded :) password is : "+ password.replace('\n','') +"\n"
                                                                print "Ended! \n"
                                                                print "Press Enter for back.\n"
                                                                qu3 = raw_input("pentest_tools >> ")
                                                                if qu3 != "KJFSDGUIOWQEU89KD237SJ7829AL83257U238472938":
                                                                                menu()
                                                elif n == 100000:
                                                                os.system('cls')
                                                                print "Cracking ! Plese Wait ...\n"
                                                                print "Tested " +str(n*y)+"/"+str(len(fr))+"\n"
                                                                n = 0
                                                                y += 1
                                                else:
                                                                n +=1
def hashid(hash1):

                                if len(hash1) ==  32 :
                                               print "hash is MD5"
                                               time.sleep(3)
                                               menu()
                                elif len(hash1) == 40:
                                                print "hash is SHA-1 // MySQL5 Hash"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==13:
                                                print "hash is DES(Unix)"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1) == 16:
                                                print "hash is MySQL // DES(Oracle Hash)"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)== 41 and hash1[0]=="*":
                                                print "hash is MySQL5"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==64:
                                                print "hash is SHA-256"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1) == 96:
                                                print "hash is SHA-384"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==128:
                                                print "hash is SHA-512"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)== 34 and hash1[0:3]=="$1$":
                                                print "hash is MD5(Unix)"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==37 and hash1[0:6]=="$apr1$":
                                                print "hash is MD5(APR)"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==34 and hash1[0:3]=="$H$":
                                                print "hash is MD5(phpBB3)"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==34 and hash1[0:3]=="$P$":
                                                print "hash is MD5(Wordpress)"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==39 and hash1[0:3]=="$5$":
                                                print "hash is SHA-256(Unix)"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==39 and hash1[0:3]=="$6$":
                                                print "hash is SHA-512(Unix)"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==24 and hash1[0:2]=="==":
                                                print "hash is MD5(Base-64)"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==28 and hash1[0]=="=":
                                                print "hash is SHA-1(Base-64)"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==40 and hash1[0:2]=="==":
                                                print "hash is SHA-224(Base-64)"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==88 and hash1[0:2]=="==":
                                                print "hash is SHA-512(Base-64)"
                                                time.sleep(3)
                                                menu()
                                elif len(hash1)==44 and hash1[0]=="=":
                                                print "hash is SHA-256(Base-64)"
                                                time.sleep(3)
                                                menu()
                                else :
                                                print "not found :("
                                                time.sleep(3)
                                                menu()
def menu():
                os.system('cls')
                os.system('color a')
                print """Select your option from the menu :
1) Encryption
2) Decryption
3) Hash Identifier
0) Exit
"""
                qu = int(raw_input("pentest_tools >> "))
                if qu == 1 :
                                os.system("cls")
                                os.system('color c')
                                print """Select your tool :
1) Password Encryptor
3) Back
"""
                                que = int(raw_input("pentest_tools >> "))
                                if que == 1:
                                                os.system('cls')
                                                print """Select your Hash Algorithm :

1) MD5
2) SHA-1
3) SHA-224
4) SHA-256
5) SHA-384
6) SHA-512
0) Back
"""
                                                que2= raw_input("pentest_tools >> ")
                                                if  que2 == '1':
                                                                os.system('cls')
                                                                print "Enter Your Password for encrypt \n"
                                                                hashs= raw_input("pentest_tools >> ")
                                                                hashencryptemd5(hashs)
                                                elif que2 == '2':
                                                                os.system('cls')
                                                                print "Enter Your Password for encrypt \n"
                                                                hashs= raw_input("pentest_tools >> ")
                                                                hashencryptemdsh1(hashs)
                                                elif que2 == '3':
                                                                os.system('cls')
                                                                print "Enter Your Password for encrypt \n"
                                                                hashs= raw_input("pentest_tools >> ")
                                                                hashencryptesha224(hashs)
                                                elif que2 == '4':
                                                                os.system('cls')
                                                                print "Enter Your Password for encrypt \n"
                                                                hashs= raw_input("pentest_tools >> ")
                                                                hashencryptesha256(hashs)
                                                elif que2 == '5':
                                                                os.system('cls')
                                                                print "Enter Your Password for encrypt \n"
                                                                hashs= raw_input("pentest_tools >> ")
                                                                hashencryptesha384(hashs)
                                                elif que2 =='6':
                                                                os.system('cls')
                                                                print "Enter Your Password for encrypt \n"
                                                                hashs= raw_input("pentest_tools >> ")
                                                                hashencryptesha512(hashs)
                                                elif que2 == '0':
                                                                menu()
                                                else:
                                                                os.system('cls')
                                                                print "Command not Found! Plese Enter from menu."
                                                                time.sleep(1)
                                                                menu()

                                elif que == 3:
                                                menu()
                                else:
                                                os.system('cls')
                                                print "Command not Found! Plese Enter from menu."
                                                time.sleep(1)
                                                menu()
                                                
                                                
                elif qu == 2 :
                                os.system('cls')
                                os.system('color d')
                                print "Enter Your Hash \n"
                                hashs2= raw_input("pentest_tools >> ")
                                if len(hashs2) == 32:
                                                pass
                                else :
                                                
                                                print "Hash not Valid!!!\n"
                                                time.sleep(1)
                                                menu()
                                print "\nEnter Your Password list \n"
                                passwordfile = raw_input('pentest_tools >>  ')
                                hashcrack(hashs2,passwordfile)
                                while 1 :
                                                os.system('cls')
                                                print "password not found :( but you can try by new wordlist.enter y for try again by new wordlist and n for end.\n"
                                                quc = raw_input('pentest_tools >> ')
                                                if quc == 'y':
                                                                os.system('cls')
                                                                print "Enter new wordlist."
                                                                passwordfile = raw_input('\npentest_tools >> ')
                                                                hashcrack(hashs2,passwordfile)
                                                elif quc != 'y':
                                                                menu()
                                os.system('cls')
                                print "Ended! hash not found:(\n"
                                print "Press Enter for back.\n"
                                qu3 = raw_input("pentest_tools >> ")
                                if qu3 != "KJFSDGUIOWQEU89KD237SJ7829AL83257U238472938":
                                                menu()
                                
                elif qu == 3:
                                os.system("cls")
                                os.system("color e")
                                print "Enter Your hash\n"
                                hash1 = raw_input("pentest_tools >> ")
                                print ""
                                hashid(hash1)
                elif qu == 0:
                                os.system('cls')
                                print "Good Bye :)"
                                time.sleep(0.5)
                                sys.exit()
                else:
                                os.system('cls')
                                print "Command not Found! Plese Enter from menu."
                                time.sleep(1)
                                menu()
                                
menu()
