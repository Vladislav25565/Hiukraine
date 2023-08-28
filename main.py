import os

# Text
whatido = "[1]Ngrok\n[2]Minecraft Server\n[3]Смійся\n>>> "
jarn = "What is the name of the server core? (example: spigot.jar)\n>>> "
bannerpath = 'plugins/banner/banner.txt'
banner2path = 'plugins/banner/banner2.txt'
banner3path = 'plugins/banner/banner3.txt'

# Read banner from file
with open(bannerpath, 'r', encoding='utf-8') as baner:
    banner = baner.read()
with open(banner3path, 'r', encoding='utf-8') as baner3:
    banner3 = baner3.read()
with open(banner2path, 'r', encoding='utf-8') as baner2:
    banner2 = baner2.read()

# Define paths and commands
ngrok = "python plugins/ngrok/ngrok.py"
cls = "clear"

# Print banner and get user input
os.system(cls)
print(banner)
wtf = input(whatido)

# Success function
def success():
    print(banner)
    os.system(cls)
    succes()

# Password check function
def check_password():
    pwd = input("Введите пароль\n\n >>>")
    if pwd == "slavaukraine":
        os.system(cls)
        success()
    else:
        os._exit(0)

# Main menu
if wtf == "1":
    os.system(cls)
    os.system(ngrok)
elif wtf == "2":
    os.system(cls)
    print(baner3)
    jarname = input(jarn)
    jar = f"java -jar plugins/jar/{jarname}"
    os.system(jar)
elif wtf == "3":
    os.system(cls)
    print(banner)
    check_password()
