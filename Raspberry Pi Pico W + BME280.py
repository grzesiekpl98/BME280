from machine import Pin, Timer, I2C
import network
import time
import utime
import urequests as requests
import machine
import urequests 
import uselect
import uctypes
import usocket
import ustruct
import urandom
import sys
import ubinascii
import rp2
import gc 
importy bme280
from secrety import secrets
import socket


led = machine.Pin("LED", machine.Pin.OUT)
led.off()

def led_blink(li,pi):
    for y in range(0, li*2):
        led.toggle()
        if y<li*2-1:
            utime.sleep(pi)
        else:
            utime.sleep(2)
            led.off()                                                                                                                                                                                                                                                                                       


rp2.country('PL')
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print('mac = ' + mac)

ssid = secrets['ssid']
pw = secrets['pw']

wlan.connect(ssid, pw)

timeout = 10
while timeout > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    timeout -= 1
    print('Waiting for connection...')
    time.sleep(1)

def blink_onboard_led(num_blinks):
    led = machine.Pin('LED', machine.Pin.OUT)
    for i in range(num_blinks):
        led.on()
        time.sleep(.2)
        led.off()
        time.sleep(.2)

wlan_status = wlan.status()
blink_onboard_led(wlan_status)

if wlan_status != 3:
    raise RuntimeError('Wi-Fi connection failed')
else:
    status = wlan.ifconfig()
    print('ip = ' + status[0])

if mac == '28:cd:c1:0b:e6:ed':
    TID = "Thermometer_ATP_0"
    corr= -3

i2c_i = I2C(0, scl=machine.Pin(5), sda=machine.Pin(4), freq=10000)
devices = i2c_i.scan()
if devices:
    for d in devices:
        print("Adres płytki termometru to: {}".format(hex(d)))

bme = bme280.BME280(i2c=i2c_i,addr=devices[0])
temp1 = bme.values[0]
temp2 = temp1.replace("C", "")
temp = float(temp2)
pressure1 = bme.values[1]
pressure2 = pressure1.replace("hPa", "")
pressure = float(pressure2)
humidity1 = bme.values[2]
humidity2 = humidity1.replace("%", "")
humidity = float(humidity2)
print("Temperature: {}".format(temp), "°C")
print("Humidity: {}".format(humidity), "%")
print("Pressure: {}".format(pressure), "hPa")
status = 0

HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = 'SGRWGLNP91C2805R'  
 
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
 
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.connect(ssid, pw)
    while not sta_if.isconnected():
     pass
print('network config:', sta_if.ifconfig()) 
 
while True:
    time.sleep(5)
    led.on()
    bme = bme280.BME280(i2c=i2c_i,addr=devices[0])
    temp1 = bme.values[0]
    temp2 = temp1.replace("C", "")
    temp = float(temp2)
    pressure1 = bme.values[1]
    pressure2 = pressure1.replace("hPa", "")
    pressure = float(pressure2)
    humidity1 = bme.values[2]
    humidity2 = humidity1.replace("%", "")
    humidity = float(humidity2)
    print("Temperature: {}".format(temp), "°C")
    print("Humidity: {}".format(humidity), "%")
    print("Pressure: {}".format(pressure), "hPa")
    
    bme_readings = {'field1':temp, 'field2':humidity, 'field3':pressure,} 
    request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + 'SGRWGLNP91C2805R', json = bme_readings, headers = HTTP_HEADERS )  
    request.close() 
    print(bme_readings) 
