import serial
import sys

"""
Class to read card from RFID
"""

class SerialReader:
	#Initializes serial with user-specified COM Port
	#in theory should work for all OS, tested with Windows 10
	
	def __init__(self, comPort):
		try:
			self.ser = serial.Serial(comPort, 9600)
		except serial.SerialException:
			print("404 Error: RFID not found")

	#Returns the ID associated with the card
	def readCard(self):
		if self.ser.isOpen():
			return self.ser.readline().decode('utf-8')[:-2]