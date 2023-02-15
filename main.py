
#Import portScanner.py
import portScanner
import speedtest
import os

hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print (hostname, 'is up!')
else:
  print (hostname, 'is down!')

# prevent the console from closing
input("Press any key to exit...")
# speedTestHelper = speedtest.Speedtest()
    
# speedTestHelper.get_best_server()

# print(speedTestHelper.download())

# if response == 0:
#   print (hostname, 'is up!')
# else:
#   print (hostname, 'is down!')

#fetch result

# print(portScanner.scanHost())
