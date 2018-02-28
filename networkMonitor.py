import time
from pythonwifi.iwlibs import Wireless

wifi = Wireless('wlp19s0')

while True:
    print wifi.getBitrate()
    time.sleep(1)

    