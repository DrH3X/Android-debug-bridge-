import os
import sys
import nmap
import socket
import colorama
from colorama import Fore
def main():
    os.system("cls")
    print(Fore.GREEN+'''
              _ _       ______            _       _ _        _   _               ______                                           _    
     /\      | | |     |  ____|          | |     (_) |      | | (_)             |  ____|                                         | |   
    /  \   __| | |__   | |__  __  ___ __ | | ___  _| |_ __ _| |_ _  ___  _ __   | |__ _ __ __ _ _ __ ___   _____      _____  _ __| | __
   / /\ \ / _` | '_ \  |  __| \ \/ / '_ \| |/ _ \| | __/ _` | __| |/ _ \| '_ \  |  __| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
  / ____ \ (_| | |_) | | |____ >  <| |_) | | (_) | | || (_| | |_| | (_) | | | | | |  | | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
 /_/    \_\__,_|_.__/  |______/_/\_\ .__/|_|\___/|_|\__\__,_|\__|_|\___/|_| |_| |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\
  ____          _____  _     _     | | _    _            _         _   _                                                               
 |  _ \        |  __ \| |   (_)    |_|| |  | |          | |       | | (_)                                                              
 | |_) |_   _  | |  | | |__  _  __ _  | |__| | __ _ _ __| | ____ _| |_ _                                                               
 |  _ <| | | | | |  | | '_ \| |/ _` | |  __  |/ _` | '__| |/ / _` | __| |                                                              
 | |_) | |_| | | |__| | | | | | (_| | | |  | | (_| | |  |   < (_| | |_| |                                                              
 |____/ \__, | |_____/|_| |_|_|\__,_| |_|  |_|\__,_|_|  |_|\_\__,_|\__|_|                                                              
         __/ |                                                                                                                         
        |___/                                                                                                                       
                        copyright © 2021 all rights reserved (Codded by dhia harkati(Dr.H3X))
                        

''')
    print(Fore.YELLOW+'1- Set pin code           10- Screen Mirroring           20- Prints all features of the device')
    print(Fore.YELLOW+'2- Set password           11- Install Apk file           21- Open url')
    print(Fore.YELLOW+'3- Set pattern code       12- Connect New Devive         22- Access shell')
    print(Fore.YELLOW+'4- Remove pin code        13- Dump device information')
    print(Fore.YELLOW+'5- Remove password        14- Adb server option')
    print(Fore.YELLOW+'6- Remove pattern code    15- List of connected devices')
    print(Fore.YELLOW+'7- Verifies the credential (pin/password/pattern correct)')
    print(Fore.YELLOW+'8- Clear the console      16- Run a specific app (require package name)')                              
    print(Fore.YELLOW+'9- Exit                   17- Package manger (app)')
    print(Fore.YELLOW+'18- Dump permissions for a specific app')
    
def adb():
    try:
        os.system("adb start-server")
        user_option=input(Fore.RED+"(Android_debug_bridge)>>")
        if user_option =='1':
            input_pin=input("Enter pin code to set :")
            os.system("adb shell locksettings set-pin " +input_pin+ "")
        elif user_option =='2':
            input_password=input("Enter password code to set :")
            os.system("adb shell locksettings set-password "+input_password+"")
        elif user_option == '3':
             input_pattern=input("Enter pattern code to set :")
             os.system("adb shell locksettings set-pattern " +input_pattern+ "")
        elif  user_option == '4':
             old_pin=input("Enter old pin code to remove :")
             os.system("adb shell locksettings clear --old "+old_pin+"")
        elif user_option == '5':
             old_password=input("Enter old password to remove :")
             os.system("adb shell locksettings clear --old "+old_password+"")
        elif user_option == '6':
             old_pattern=input("Enter old pattern to remove :")
             os.system("adb shell locksettings clear --old "+old_pattern+"")
        elif user_option == '8':
             os.system("cls")
             main()
        elif user_option == '7':
             code_verify=input("Enter (pin/password/pattern) to verify :")
             os.system("adb shell locksettings verify --old "+code_verify+"")
        elif user_option== '9':
             sys.exit()
        elif user_option== '10':
            print(Fore.GREEN+'[+]Starting scrcpy service')
            os.system("scrcpy")
        elif user_option=='11':
             dir_of_apk=input("Directory of the apk file :")
             os.system("adb install "+dir_of_apk+"")
        elif user_option=='12':
             ip= input('Enter ip address : ')
             print('checking for ip address state')
             scanner = nmap.PortScanner()
             host = socket.gethostbyname(ip)
             scanner.scan(host, '1', '-v')
             print("IP Status: ", scanner[host].state())
             if scanner[host].state()=='up':
                 print('checking for port 5555')
                 scanner = nmap.PortScanner()
                 res = scanner.scan(ip,str(5555))
                 res = res['scan'][ip]['tcp'][5555]['state']  
                 print(f'port {5555} is {res}.')
                 if res=='open':
                     print('connecting to the device in progress')
                     os.system("adb tcpip 5555")
                     os.system("adb connect "+ip+":5555")
                 elif res=='filtred':
                     print('cannot connect to the device')
                 elif res=='close':
                     print('cannot connect to the device')
             elif scanner[host].state()=='down':
                 print('device offline cannot connect')
        elif user_option=='13':
            user_choice=input('Run android debug bridge over tcp/ip or usb >>')
            if user_choice=='tcp/ip':
                input_ip=input("Ip address :")
                os.system("adb -s "+input_ip+" shell getprop")
            elif user_choice=='usb':
                print('serialno :'),os.system("adb shell getprop ro.serialno")
                serialno=input("input serialno : ")
                os.system("adb -s "+serialno+" shell getprop ")
        elif user_option=='14':
            print('1-Start the server')
            print('2-Kill the server')
            print('3-kick connection from device side (phone) to force reconnect')
            print('4-Kick connection from host side (Computer) to force reconnect')
            print('5-reset offline/unauthorized devices to force reconnect')
            print('6- back to Android_debug_bridge option')
            server_option=input(Fore.BLUE+"(Server_option)>>")
            if server_option=='1':
                os.system("adb start-server")
            elif server_option=='2':
                os.system("adb kill-server")
            elif server_option=='3':
                os.system("adb reconnect")
            elif server_option=='4':
                os.system("adb reconnect device")
            elif server_option=='5':
                os.system("adb reconnect offline")
            elif server_option=='7':
                os.system("cls")
                main()
        elif user_option=='15':
            os.system("adb devices -l ")
        elif user_option=='16':
            device_name1=input("Enter Device name (ip/serialno) : ")
            package_name=input("Enter the first character of the specific app :")
            os.system("adb -s "+device_name1+" shell pm list package "+package_name+"")
            specific_app=input("Enter the package name :")
            os.system("adb -s "+device_name1+" shell monkey -p "+specific_app+" -v 500")
        elif user_option=='17':
            print('1- All the packages of this devcie                     9-  Enable specific app')
            print('2- Files associated with the installation package      10- Disable specific app')
            print('3- All the system package name                         11- Get path for specific app')
            print('4- Third-party installation packages                   12- Search for specific package name')
            print('5- Packages disabled by this device                    13- Permission manger')
            print('6- Packages enabled by this device                     14- Dump list of permission for specifc app(.apk)')
            print('7- Unistall specific app (package name)')
            print('8- Deletes all data associated with a package')
            input_option1=input(Fore.BLUE+"(package_manger)>>")
            device_name2=input("Enter device name (ip/serialno) :")
            if input_option1=='1':
                os.system("adb -s "+device_name2+" shell pm list packages")
            elif input_option1=='2':
                os.system("adb -s "+device_name2+" shell pm list packages -f")
            elif input_option1=='3':
                os.system("adb -s "+device_name2+" shell pm list packages -s")
            elif input_option1=='4':
                os.system("adb -s "+device_name2+" shell pm list packages -3")
            elif input_option1=='5':
                os.system("adb -s "+device_name2+" shell pm list packages -d")
            elif input_option1=='6':
                os.system("adb -s "+device_name2+" shell pm list packages -e")
            elif input_option1=='7':
                unistall=input("Enter package name to delete :")
                os.system("adb -s "+device_name2+" shell pm unistall "+unistall+"")
            elif input_option1=='8':
                package=input("Enter package name to clear associated data :")
                os.system("adb -s "+device_name2+" shell pm clear "+package+"")
            elif input_option1=='9':
                nameofpackage=input("Enter package name to enable :")
                os.system("adb -s "+device_name2+" shell pm enable "+nameofpackage+"")
            elif input_option1=='10':
                nameofpackage=input("Enter package name to disable :")
                os.system("adb -s "+device_name2+" shell pm disable "+nameofpackage+"")
            elif input_option1=='11':
                nameofpackage=input("Enter package name to get the path (path of the apk file):")
                os.system("adb -s "+device_name2+" shell pm path "+nameofpackage+"")
            elif input_option1=='12':
                firstcharofpackage=input("Enter first character of the package name to search :")
                os.system("adb -s "+device_name2+" shell pm list package "+firstcharofpackage+"")
            elif input_option1=='13':
                print('1- reset-permissions for specific app')
                print('2- Grant permissions for specific app')
                print('3- Revoke (remove) permissions for specific app')
                permission_choice=input(Fore.BLUE+"(Permission_manger)>>")
                device_name3=input("Enter device name (ip/serialno) :")
                if permission_choice=='1':
                    packagename=input("Enter package name to revert all runtime permissions to their default state :")
                    os.system("adb -s "+device_name3+" shell pm reset-permissions "+packagename+"")
                elif permission_choice=='2':
                    print('Search for list of permission by filter :')
                    print('1- Print all information')
                    print('2- Only list dangerous permissions')
                    print('3- List only the permissions users will see')
                    print('4- List of permission Organize by group')
                    permission_filter=input("Choice filter to search :")
                    if permission_filter=='1':
                        os.system("adb -s " +device_name3+" shell pm list permissions -f ")
                        package_grant=input("Enter package name to grant permission :")
                        grant_permission=input("Choice a permission to grant :")
                        os.system("adb -s " +device_name3+" shell pm grant "+package_name+" "+grant_permission+"")
                    elif permission_filter=='2':
                        os.system("adb -s " +device_name3+" shell pm list permissions -d ")
                        package_grant=input("Enter package name to grant permission :")
                        grant_permission=input("Choice a permission to grant :")
                        os.system("adb -s " +device_name3+" shell pm grant "+package_name+" "+grant_permission+"")
                    elif permission_filter=='3':
                        os.system("adb -s " +device_name3+" shell pm list permissions -u ")
                        package_grant=input("Enter package name to grant permission :")
                        grant_permission=input("Choice a permission to grant :")
                        os.system("adb -s " +device_name3+" shell pm grant "+package_name+" "+grant_permission+"")
                    elif permission_filter=='4':
                        os.system("adb -s " +device_name3+" shell pm list permissions -g")
                        package_grant=input("Enter package name to grant permission :")
                        grant_permission=input("Choice a permission to grant :")
                        os.system("adb -s " +device_name3+" shell pm grant "+package_name+" "+grant_permission+"")
                elif permission_choice=='3':
                    print('Search for list of permission by filter :')
                    print('1- Print all information')
                    print('2- Only list dangerous permissions')
                    print('3- List only the permissions users will see')
                    print('4- List of permission Organize by group')
                    permission_filter1=input("Choice filter to search :")
                    if permission_filter1=='1':
                        os.system("adb -s " +device_name3+" shell pm list permissions -f ")
                        package_revoke=input("Enter package name to grant permission :")
                        revoke_permission=input("Choice a permission to grant :")
                        os.system("adb -s " +device_name3+" shell pm grant "+package_revoke+" "+revoke_permission+"")
                    elif permission_filter1=='2':
                        os.system("adb -s " +device_name3+" shell pm list permissions -d ")
                        package_revoke=input("Enter package name to grant permission :")
                        revoke_permission=input("Choice a permission to grant :")
                        os.system("adb -s " +device_name3+" shell pm grant "+package_revoke+" "+revoke_permission+"")
                    elif permission_filter1=='3':
                        os.system("adb -s " +device_name3+" shell pm list permissions -u ")
                        package_revoke=input("Enter package name to grant permission :")
                        revoke_permission=input("Choice a permission to grant :")
                        os.system("adb -s " +device_name3+" shell pm grant "+package_revoke+" "+revoke_permission+"")
                    elif permission_filter1=='4':
                        os.system("adb -s " +device_name3+" shell pm list permissions -g")
                        package_revoke=input("Enter package name to grant permission :")
                        revoke_permission=input("Choice a permission to grant :")
                        os.system("adb -s " +device_name3+" shell pm grant "+package_revoke+" "+revoke_permission+"")
        elif user_option=='22':
            device_name5=input("Enter devcie name (ip/serailno) :")
            os.system("adb -s "+device_name5+" shell ")
        elif user_option=='20':
            device_name4=input("Enter Device name (ip/serialno) :")
            print('List of all features available for this device :')
            os.system("adb -s "+device_name4+" shell pm list features")
        elif user_option=='21':
            url_device_name=input("Enter_device_name(ip/serialno)>>")
            url=input("Enter_url_to_open>>")
            os.system("adb -s "+url_device_name+" shell am start -a android.intent.action.VIEW -d "+url+"")
    except KeyboardInterrupt:
        print('Interrupt')
while True:
    adb()


    


        


    
    

    



    
    
    
    
    
    
    
    
           
           




