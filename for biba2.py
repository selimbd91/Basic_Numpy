
def fun():
    string ="""(Sun Sep 13 23:02:05 2009): Beginning Wbemupgd.dll Registration

(Sun Sep 13 23:02:05 2009): Beginning Processing .\info.json Core Upgrade

(Sun Sep 13 23:02:05 2009): Beginning MOF load

(Sun Sep 13 23:02:05 2009): Processing C:\WINDOWS\system32\WBEM\cimwin32.mof

(Sun Sep 13 23:02:09 2009): Processing C:\WINDOWS\system32\WBEM\cimwin32.mfl

(Sun Sep 13 23:02:12 2009): Processing C:\WINDOWS\system32\WBEM\system.mof

(Sun Sep 13 23:02:16 2009): Processing C:\WINDOWS\system32\WBEM\evntrprv.mof

(Sun Sep 13 23:02:16 2009): Processing C:\WINDOWS\system32\WBEM\hnetcfg.mof

(Sun Sep 13 23:02:16 2009): Processing C:\WINDOWS\system32\WBEM\sr.mof

(Sun Sep 13 23:02:16 2009): Processing C:\WINDOWS\system32\WBEM\dgnet.mof

(Sun Sep 13 23:02:16 2009): Processing C:\WINDOWS\system32\WBEM\whqlprov.mof

(Sun Sep 13 23:02:16 2009): Processing C:\WINDOWS\system32\WBEM\ieinfo5.mof

(Sun Sep 13 23:02:17 2009): MOF load completed.

(Sun Sep 13 23:02:17 2009): Beginning MOF load

(Sun Sep 13 23:02:17 2009): MOF load completed.

(Sun Sep 13 23:02:17 2009): Core Upgrade completed.

(Sun Sep 13 23:02:17 2009): Wbemupgd.dll Service Security upgrade succeeded.

(Sun Sep 13 23:02:17 2009): Beginning WMI(WDM) Namespace Init

(Sun Sep 13 23:02:20 2009): WMI(WDM) Namespace Init Completed

(Sun Sep 13 23:02:20 2009): ESS enabled

(Sun Sep 13 23:02:20 2009): ODBC Driver <system32>\wbemdr32.dll not present

(Sun Sep 13 23:02:20 2009): Successfully verified WBEM OBDC adapter (incompatible.

(Sun Sep 13 23:02:20 2009): Wbemupgd.dll Registration completed.

(Sun Sep 13 23:02:20 2009):"""

    print(string[18:20])
    num1 = int(string[19:21])
    print(string[-9:-7])
    num2 = int(string[-9:-7])
    print(f"The Duration of the logged application {num2 - num1}")

    print(f"First Programm is done.................")


    #print(string[29])
    str2 = string.split("\n")
    #print(str2)

    my_list = []
    for i in str2:
        if "Beginning Processing" in i:
            my_list.append(i)
            #print(i)
        if "Processing C:" in i:
            my_list.append(i)
            #print(i)
        if "ODBC Driver" in i:
            my_list.append(i)
            #print(i)

    print(my_list)

    print("The second programm is done...................")

    my_list2 = []

    for j in str2:
        #if ".dll" in j:
            #my_list2.append(j)
             #print(j)
    #print(my_list2)

    #str3 = " ".join(my_list2)
    #print(str3)

    #list4 = str3.split(":")
    #print(list4)

    #for k in range(0,len(list4)):





def main():
    fun()

if __name__ == "__main__":
    main()