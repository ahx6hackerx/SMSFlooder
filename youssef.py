import argparse
import sys
import signal
import os

class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
#this simple function will handle signal
def attack_handler(signal, frame):
    print(bcolors.WARNING + '\n[!]Stopping the Attack.')
    os._exit(0)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=str, metavar=" Target phone",
                        help="phone Number.")
    parser.add_argument("--flood", type=str, metavar="SMS",
                        help="SMS and calls flooding maybe i will add another modules")
    parser.add_argument("--timeout", type=int, default=10, metavar="timeout",
                        help='Timeout attack')
    parser.add_argument("--threads", type=int, default=3, metavar="threads",
                        help="Threads to send.")





    args = parser.parse_args()
    threads = args.threads
    time = args.timeout
    attack = str(args.flood).upper()
    target = args.target
    if attack == "SMS":
        signal.signal(signal.SIGINT, attack_handler)
        import tools.zina.clear
        import tools.zina.zina
        from tools.SMS.main import SMS_ATTACK
        SMS_ATTACK(threads, time, target)
    else:
        parser.print_help()

if __name__ == '__main__':
     main()

