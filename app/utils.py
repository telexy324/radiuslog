from datetime import datetime
from time import mktime


def string2timestamp(strValue):

    try:
        d = datetime.strptime(strValue, "%Y-%m-%d %H:%M")
        t = d.timetuple()
        timeStamp = int(mktime(t))
        return timeStamp+28800
    except Exception as e:
        print e
        return ''


def timestamp2string(timeStamp):
    try:
        d = datetime.fromtimestamp(timeStamp-28800)
        str1 = d.strftime("%Y-%m-%d %H:%M:%S")
        return str1
    except Exception as e:
        print e
        return ''