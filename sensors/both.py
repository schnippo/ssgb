#returns both 1W and I2C sensor values - only one I2C device


import glob, os, adafruit_dht, datetime
from time import sleep
## ONEWIRE SETUP
os.system('modprobe w1-gpio')                              # load one wire communication device kern$
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'                          # point to the address
device_folder = glob.glob(base_dir + '28*')[0]             # find device with address starting from $
device_file = device_folder + '/w1_slave' 
logfile_air_temp = "log_air_temp.txt"
logfile_air_hum = "log_air_hum.txt"
logfile_water_temp = "log_water_temp.txt"

def reset_file(file):
   f = open(file, "w")
   f.write("")
   f.close

# store the details
def read_temp_raw():
   f = open(device_file, 'r')
   lines = f.readlines()                                   # read the device details
   f.close()
   return lines

def read_temp():
   lines = read_temp_raw()
   while lines[0].strip()[-3:] != 'YES':                   # ignore first line
      sleep(0.2)
      lines = read_temp_raw()
   equals_pos = lines[1].find('t=')                        # find temperature in the details
   if equals_pos != -1:
      temp_string = lines[1][equals_pos+2:]
      temp_c = float(temp_string) / 1000.0                 # convert to Celsius
      return temp_c

## I2C Setup = temp and hum sensor
dht_device = adafruit_dht.DHT22(2)

reset_file(logfile_air_temp)
reset_file(logfile_air_hum)
reset_file(logfile_water_temp)

while True:
   logat = open(logfile_air_temp, "a")
   logah = open(logfile_air_hum, "a")
   logwt = open(logfile_water_temp, "a")
      for i in range(6)
         now = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
         logat.write(now+":"+str(dht_device.temperature))
         logah.write(now+":"+str(dht_device.humidity))
         logwt.write(now+":"+str(read_remp))
        sleep(5)
