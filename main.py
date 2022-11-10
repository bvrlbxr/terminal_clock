import datetime,time,os
from art import *

def terminal_clock():
	flag = True
	while True:

		if flag:
			formation = "   %H : %M"			
		else:
			formation = "   %H     %M"
			
		flag = not flag
		
		cur_time = datetime.datetime.now().strftime(formation)
		tprint(cur_time)
		time.sleep(0.5)
		os.system("cls")

if __name__ == '__main__':
	terminal_clock()
