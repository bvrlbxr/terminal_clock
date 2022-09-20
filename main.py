import datetime,time,os
from art import *

def terminal_clock():
	flag = True
	while True:

		if flag is True:
			formation = "   %H : %M"
			flag = False

		elif flag is False:
			formation = "   %H     %M"
			flag = True

		cur_time = datetime.datetime.now().strftime(formation)
		tprint(cur_time)
		time.sleep(0.5)
		os.system("cls")

if __name__ == '__main__':
	terminal_clock()