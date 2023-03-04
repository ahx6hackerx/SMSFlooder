import os
def install():
    try:
        import setuptools
        os.system("pip3 install -r req.txt")
        print("you are ready run python3 youssef.py -h")
    except ModuleNotFoundError:
        if os.getuid() == 0:
            os.system("apt-get install python3-pip")
            os.system("pip3 install -r req.txt")
            print("you are ready run python3 youssef.py -h")

        else:
            print("you are linux user run as root to install the package")
install()
if 'ANDROID_BOOTLOGO' in os.environ:
    try:
        import setuptools
        os.system("pip3 install -r req.txt")
        print("you are ready run python3 youssef.py -h")
    except ModuleNotFoundError:
        os.system("pkg i python3")
        os.system("pip3 install -r req.txt")
        print("you are ready run python3 youssef.py -h")



