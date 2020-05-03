import os
import platform
import socket
import sys
import time
import subprocess
import colorama
from colorama import Fore,Back,Style,init
import datetime
colorama.init()
try:
    import nmap
except ModuleNotFoundError :
    print(Fore.YELLOW+"\n Looks like you've not installed modules. Try running 'pip install -r requirements.txt'.\n"+Style.RESET_ALL)
except NameError :
    print(Fore.YELLOW+"\n Looks like you've not installed modules. Try running 'pip install -r requirements.txt'.\n"+Style.RESET_ALL)


try:
    
    Sc = nmap.PortScanner()
    def greet():
        
        print(Fore.MAGENTA+'THANK YOU FOR USING OUR TOOL : )')
        print('')
        quit()

    def upstat():
         print('')
         print(Fore.GREEN+"Host is UP +++++++++"+Style.RESET_ALL)
    def dowstat():
            print('')
            print(Fore.RED+"Host is DOWN --------"+Style.RESET_ALL)
            print('')
            
    def clear():
        if os.name == 'nt':
                os.system("cls")
        else:
                os.system('clear')
    def stat():
        print("\n")
        print(Fore.YELLOW+"Target IP Address:  ",end=''+Style.RESET_ALL)
        global ipaddr
        ipaddr = input('')
        print('')
        print(Fore.CYAN)
        global response
        response = os.system("ping  " + ipaddr)
        print(Style.RESET_ALL)
    
  
        
    
    def logo():
        print("")
        print(Fore.YELLOW+'''      \t\t sssss ccccc     a    n n    n   n n    n  yy   yy
                 s     c        a a   n  n   n   n  n   n   yy yy
                 sssss c       a a a  n    n n   n    n n    yy'''+Style.RESET_ALL)
        print(Fore.RED+'''      \t\t     s c      a     a n      n   n      n    yy   
                 sssss ccccc a       an      n   n      n    yy '''+Style.RESET_ALL)  
        print(Fore.CYAN+"version - 1.0"+Style.RESET_ALL)
        print(Fore.YELLOW+'CREDiTS : Abhiram.M') 
        print('')          
  
    def barricade():
         print(Fore.BLUE+Style.BRIGHT+"<----------------------------------------------------------->"+Style.RESET_ALL)
    
    def ti():
         global x
         x = datetime.datetime.now()
         print(Fore.CYAN+'started scan on\t'+str(x)+Style.RESET_ALL )
         print("")

    def eti():
            global y
            y = datetime.datetime.now()
            print(Fore.CYAN+'Ended scan on\t'+str(y)+Style.RESET_ALL )
            print("\n")
  
   
    def out():
     
      hosts = Sc.all_hosts()
        
      for h in hosts :
        print(Fore.YELLOW+"[+] Scanned hosts:",h,"(",Sc[h].hostname(),")"+Style.RESET_ALL)
        proto = Sc[h].all_protocols()
        for prot in proto:
            print(Fore.YELLOW+"[+] Protocols : ",prot+Style.RESET_ALL)
            print('')
            oport = Sc[h][prot].keys()
            sorted(oport)
            num = 1
            for port in oport:
                 protocol = 'tcp'
                 
                 print(Fore.GREEN+'', num,']',' port : %d\tstate : %s' % (port, Sc[h][prot][port]['state'])+Style.RESET_ALL)
                 try:
                  print(Fore.GREEN+'Service :',socket.getservbyport(port,protocol)+Style.RESET_ALL)
                 except:
                     print(Fore.RED+'Service : unknown'+Style.RESET_ALL)
                     num = num+1
                     print('')
                     continue
                     
  
                 num = num+1
               
                 print('')
      print(Style.RESET_ALL)
    def udpout():
        print('')
      
        
        hosts = Sc.all_hosts()
       
        global h
        
        for h in hosts :
         print(Fore.YELLOW+"[+] Scanned hosts:",h,"(",Sc[h].hostname(),")"+Style.RESET_ALL)
         global proto
         proto = Sc[h].all_protocols()
         for prot in proto:
            print(Fore.YELLOW+"[+] Protocols : ",prot+Style.RESET_ALL)
            print('')
            
            oport = Sc[h][prot].keys()
            sorted(oport)
            num = 1
            for port in oport:
                 protocol = 'udp'
                 
                 print(Fore.GREEN+'',num,']',' port : %d\tstate : %s' % (port, Sc[h][prot][port]['state'])+Style.RESET_ALL)
                 try:
                  print(Fore.GREEN+'Service :',socket.getservbyport(port,protocol)+Style.RESET_ALL)
                  num = num+1
                  print('')
                  continue
                              
                 except:
                     print(Fore.RED+'Service : unknown'+Style.RESET_ALL)
                     num = num+1
                     print('')
                     continue
    
    def mixudp():
       
        print('')
        hosts = Sc.all_hosts()
       
        global h
        
        for h in hosts :
         
         global proto
         proto = Sc[h].all_protocols()
         for prot in proto:
            print(Fore.YELLOW+"[+] Protocols : ",prot+Style.RESET_ALL)
            print('')
            
            oport = Sc[h][prot].keys()
            sorted(oport)
            num = 1
            nb = 0
            for port in oport:
                 protocol = 'udp'
                 
                 print(Fore.GREEN+'',num,']',' port : %d\tstate : %s' % (port, Sc[h][prot][port]['state'])+Style.RESET_ALL)
                 try:
                  print(Fore.GREEN+'Service :',socket.getservbyport(port,protocol)+Style.RESET_ALL)
                  num = num+1
                  print('')
                  nb = nb+1
                  continue
                              
                 except:
                     print(Fore.RED+'Service : unknown'+Style.RESET_ALL)
                     num = num+1
                     print('')
                     nb = nb+1
                     continue
          
   
    print(Fore.BLUE + "\nWELCOME TO SCANNY , A AUTOMATED TOOL FOR PORT SCANNING >>>> " + Style.BRIGHT +Style.RESET_ALL + "\n")
    print(Fore.GREEN+'Select what you want to do :'+Style.BRIGHT+Style.RESET_ALL)
    print(Fore.YELLOW+Style.BRIGHT+" ", " ", "1) SYN ACK Scanning ")
    print(" ", " ", "2) UDP Scanning ")
    print(" ", " ", "3) Comprehensive Scanning Or Aggressive scanning  ")
    print(" ", " ", "4) FIN Scanning  ")
    print(" ", " ", "5) IP Status Checker ")
    print(" ", " ", "6) Custom Port Scanner " +Style.RESET_ALL)
 
    
    barricade()
    
    print(Fore.RED + "##########  ",end=''+Style.RESET_ALL)
    scanningopt = input()
    print(Fore.MAGENTA + Style.DIM +"You have selected option no."+Style.RESET_ALL, scanningopt)
    barricade()
    clear()
   
   # print(Sc[ipaddr].hostname())
   # print(Sc[ipaddr].state())
    #print(Sc[ipaddr].all_protocols())
    #print(Sc[ipaddr]['tcp'].keys())
    #print(Sc[ipaddr]['tcp'].keys())
 
    if scanningopt == '1':
        print('\n')
        logo()    
        barricade()
        stat()
        if response == 0:
            upstat()
            barricade()
            ti()
            
            print(Fore.GREEN + "Starting SYN-ACK Scan....../" + Style.RESET_ALL)
            print(Fore.RED+'\n [ NOTE: Be patient. It will take 2-3 mins. ]\n ')
            sc1 = Sc.scan(ipaddr, '22-443', ' -sS')
            sc1_2=Sc.scan(ipaddr,'22-443','-T5')
            out()
            
            eti()
            greet()
        else:
             dowstat()
             greet()
    
    elif scanningopt == '2':
        print("\n")
        logo()
        barricade()
        stat()
        if response == 0:
            upstat()
            barricade()
            ti()

            print(Fore.GREEN + "Starting UDP Scan....../" + Style.RESET_ALL)
            print(Fore.RED+'\n[ NOTE: Be patient. It will take 7-8 mins. ] \n'+Style.RESET_ALL)
            sc2 = Sc.scan(ipaddr, '22-443','-T5')
            Sc2_2 =Sc.scan(ipaddr,'22-443','-sU')
            udpout()
            eti()
            greet()
        else:
            dowstat()
            greet()
    elif scanningopt == '3':
        print('\n')
        logo()
        barricade()
        barricade()
        stat()

        
        if response == 0:
            upstat()
            barricade()
            ti()
            print(Fore.GREEN+'Started Comprehensive Scanning ....../'+Style.RESET_ALL)
            print(Fore.RED+'\n [ Note: Be patient. It will take 20-25 mins. ]\n'+Style.RESET_ALL)
            barricade()
            print(Fore.YELLOW+'Scanning TCP ports...'+Style.RESET_ALL)
            print('')
            sc3 = Sc.scan(ipaddr,'1-1024','-A')
            sc3_0  = Sc.scan(ipaddr,'1-1024','T5')
            sc3_1 = Sc.scan(ipaddr,'1-1024','-sS')
            sc3_3 = Sc.scan(ipaddr,'1-1024','-O')
            out()
            barricade()
            print(Fore.YELLOW+'Scanning UDP ports...'+Style.RESET_ALL)
           
            sc3_2 = Sc.scan(ipaddr,'1-1024','-sU')
            mixudp()
            eti()
            greet()
        else:
           dowstat()
           greet()

   
       
    elif scanningopt == '4':
        print("\n")
        logo()
        barricade()
        stat()
       
        if response == 0:
            upstat()
            barricade()
            ti()
            print(Fore.GREEN+'Started FIN Scanning....../'+Style.RESET_ALL)
            print(Fore.RED+'[\n NOTE: Be patient. It will take around 10 mins. ] \n'+Style.RESET_ALL)
            sc5 = Sc.scan(ipaddr, '1-1024', ' -sN')
            sc5_1 = Sc.scan(ipaddr,'1-1024','-T5')
            out()
            eti()
            greet()
        else:
             dowstat()
             greet()


    elif scanningopt == '5':
        
        logo()
        barricade()
        print(Fore.GREEN+'Started IP STATUS CHECKER'+Style.RESET_ALL)
        
        stat()
        if response == 0:
            upstat()
            barricade()
            greet()
        else:
            dowstat()
            greet()
    elif scanningopt == '6':
            
            logo()
            barricade()
            stat()
            barricade()
            
            if response == 0:
                upstat()
                barricade() 
                ti()
                print(Fore.GREEN+'Started CUSTOM Port Scanner ...../'+Style.RESET_ALL)
                print(Fore.RED+'\n NOTE: If you want to scan specific port, Enter that port in first input and enter "0" in second input.And please be atient because the more the range is ,The more time will be taken \n '+Style.RESET_ALL)
                print(Fore.GREEN+'Enter the range of ports you want to scan : '+Style.RESET_ALL )
                print(Fore.RED+'>>>>> ',end=''+Style.RESET_ALL)
                poran1 = input()
                print(Fore.RED+'>>>>> ',end=''+Style.RESET_ALL)
                poran2 = input()
                if poran2 == 0:
                    poran2 = poran1
                poran = (poran1+'-'+poran2)
                ranpo = poran.replace('()',"") and poran.replace(',','')
                barricade()
                sc7 = Sc.scan(ipaddr,ranpo,'-v')
                out()
                eti()
                greet()
            else:
              dowstat()
              greet()

except KeyboardInterrupt:
    print(Fore.RED+"\n[!] Looks like you've pressed ctrl-c .Please run the tool again\n"+ Style.RESET_ALL)
