import os
import sys
import httplib2
import socket
import ssl
import shift_planning
import credentials as creds
from UserFactory import UserFactory

def isConnected():
    try:
        host = socket.gethostbyname("inventionstudio.humanity.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        e = sys.exc_info()[0]
        print str(e)
    return False

def getUsers():
    s = shift_planning.ShiftPlanning(creds.HUMANITY_KEY, creds.HUMANITY_LOGIN, creds.HUMANITY_PASSWORD)
    s.do_login()
    s.get_employees()
    uf = UserFactory('users.csv')
    for e in s.get_public_data():
        firstname = e["firstname"]
        lastname = e["lastname"]
        if firstname is None:
            firstname = ""
        if lastname is None:
            lastname = ""
        else:
            lastname = lastname + ", "
        uf.write(e['id'], e['firstname'], e['lastname'], e['username'], 0)

def getUserStatus(userid):
    s = shift_planning.ShiftPlanning(creds.HUMANITY_KEY, creds.HUMANITY_LOGIN, creds.HUMANITY_PASSWORD)
    s.do_login()

    s.get_timeclock_status(userid, 0)
    for e in s.get_public_data():
        status = e["status"]
        print str(status)

if __name__ == "__main__":
	  print "Connection Status: " + str(isConnected())
