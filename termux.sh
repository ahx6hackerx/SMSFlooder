if ! which python > /dev/null; then
   echo -e "[!] python not found! Installing"
   sleep 2
   pkg  install python
   python3 install.py
   
else
   echo -e "[+] python already installed installing script req"
   sleep 2
   python3 install.py
fi
