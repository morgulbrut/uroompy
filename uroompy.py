import serial

class Roomba():

	C_START = 128
	C_BAUD = 129
	C_SAFE = 131
	C_FULL = 132
	C_OFF = 0
		# Cleaning Commands
	C_CLEAN = 135
	C_MAX = 136
	C_SPOT = 134
	C_SEEK_DOCK = 143
	C_SCHEDULE = 167
	C_SET_TIME = 168
	C_POWER = 133
		# Actuator Commands
	C_DRIVE = 137
	C_DRIVE_DIRECT = 145
	C_DRIVE_PWW = 146
	C_MOTORS = 138
	C_PWM_MOTORS = 144
	C_LEDS = 139
	C_SCHEDULING_LED = 162
	C_DIGIT_LEDS_RAW = 163
	C_DIGIT_LEDS_ASCII = 164
	C_BUTTONS = 165
	C_SONG = 140
	C_PLAY = 141
		# Input Commands
	C_SENSORS = 142
	C_QUERY_LIST = 149
	C_STREAM = 148
	C_PAUSE_STREAM = 150
	 	#Sensor Packets
	SP_BUMPS_AND_WHEELS = 7
	SP_WALL = 8
	SP_CLIFF_LEFT = 8
	SP_CLIFF_FRONT_LEFT = 10
	SP_CLIFF_FRONT_RIGHT = 11
	SP_CLIFF_RIGHT = 12
	SP_VIRTUAL_WALL = 13
	SP_WHEEL_OVERCURRENT = 14
	SP_DIRT_DETECT = 15
	SP_INFRARED_CHAR_OMNI = 17
	SP_INFRARED_CHAR_LEFT = 52
	SP_INFRARED_CHAR_RIGHT = 53
	SP_BUTTONS = 18
	SP_DISTANCE = 19
	SP_ANGLE = 20
	SP_CHARGING_STATE = 21
	SP_VOLATAGE = 22
	SP_CURRENT = 23
	SP_TEMPERATURE = 24
	SP_BATTERY_CHARGE = 25
	SP_BATTERY_CAPACITY = 26
	SP_WALL_SIGNAL = 27
	SP_CLIFF_LEFT_SIGNAL = 28
	SP_CLIFF_FRONT_LEFT_SIGNAL = 28
	SP_CLIFF_FRONT_RIGHT_SIGNAL = 28
	SP_CLIFF_RIGHT_SIGNAL = 28
	SP_CHARGING_AVAILABLE = 34
	SP_OI_MODE = 35
	SP_SONG_NUMBER = 36
	SP_SONG_PLAYING = 37
	SP_NO_OF_STREAM_PACKETS = 38
	SP_REQUESTED_VELOCITY = 39
	SP_REQUESTED_RADIUS = 40
	SP_REQUESTED_RIGHT_VELOCITY = 41
	SP_REQUESTED_LEFT_VELOCITY = 42
	SP_RIGHT_ENCODER_COUNTS = 43
	SP_LEFT_ENCODER_COUNTS = 44
	SP_LIGHT_BUMPER = 45
	SP_LIGHT_BUMP_LEFT_SIGNAL = 46
	SP_LIGHT_BUMP_FRONT_LEFT_SIGNAL = 47
	SP_LIGHT_BUMP_CENTER_LEFT_SIGNAL = 48
	SP_LIGHT_BUMP_CENTER_RIGHT_SIGNAL = 49
	SP_LIGHT_BUMP_FRONT_RIGHT_SIGNAL = 50
	SP_LIGHT_BUMP_RIGHT_SIGNAL = 51
	SP_LEFT_MOTOR_CURRENT = 54
	SP_RIGHT_MOTOR_CURRENT = 55
	SP_MAIN_BRUSH_MOTOR_CURRENT = 56
	SP_SIDE_BRUSH_MOTOR_CURRENT = 57
	SP_STASIS = 58

	def  __init__(self,port,baud,mode=C_SAFE):

		self.serial = serial.Serial(
			port = port,
			baudrate = baud)
		
		self.send_command(self.C_START)
		if mode == self.FULL:
			self.send_command(self.C_FULL)
		elif mode == self.OFF:
			self.send_command(self.C_START)
		else:
			self.send_command(self.C_SAFE)
	

	def drive(self, velocity = 0, radius = 0):
		pass 

	def stop(self):
		self.drive()

	def read_sensor(self, sensor):
		command = self.C_SENSORS + sensor
		self.send_command(command)

	def set_schedule(self,time):
		pass

	def send_command(self,command):
		print('[CMD]: '+str(command))
		self.serial.write(command)

	def connect_serial(self,port,baud):
		print('[UART]: connecting')
		self.serial = serial.Serial(
			port = port,
			baudrate = baud)