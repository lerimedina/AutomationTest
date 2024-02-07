#import win32clipboard
#win32clipboard.OpenClipboard()
#win32clipboard.EmptyClipboard()
#win32clipboard.SetClipboardText("once this is saved theres no turning back")
#win32clipboard.CloseClipboard()

#import os
#os.system('cd')

#import subprocess
#proc = subprocess.Popen('cmd.exe')
#proc.communicate('cd Documents')

#import subprocess
#proc = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)
#proc.stdin.write(b'cd pythontestst\n')

# import powertop

# measures = powertop.Powertop().get_measures(time=1, iterations=1)

import AppOpener as ao

# ao.open("sublime text")
# ao.mklist(name="app_data.json")

app_names = ao.give_appnames()
# apps=["notepad", "sublime", "chrome"]

# list of apps in the machine
ao.open("ls")


# for app in apps:
#     ao.open(app, match_closest=True)


# ao.mklist(name="txt_format.txt")


# to launch multiple applications
# num = int(input("Enter number of apps: "))
# for i in range(1,num+1):
#     prog = input("Enter application: ")
#     ao.open(prog, match_closest=True)
    