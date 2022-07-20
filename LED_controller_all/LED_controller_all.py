#!/usr/bin/env python 3

from flask import Flask, render_template, url_for, redirect
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin_dict = {'red': 14, 'yellow': 15, 'blue': 18}
GPIO.setup(led_pin_dict['red'], GPIO.OUT)
GPIO.setup(led_pin_dict['yellow'], GPIO.OUT)  
GPIO.setup(led_pin_dict['blue'], GPIO.OUT)
led_state_dict = {'red':0, 'yellow':0, 'blue':0}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('all_btn.html', led_state_dict = led_state_dict)  

@app.route('/all/<int:state>')
def whole_control(state):
    if state == 0:
        led_state_dict['red']=0
        led_state_dict['yellow']=0
        led_state_dict['blue']=0 
    elif state == 1: 
        led_state_dict['red']=1
        led_state_dict['yellow']=1
        led_state_dict['blue']=1 
    GPIO.output(led_pin_dict['red'], led_state_dict['red']) 
    GPIO.output(led_pin_dict['yellow'], led_state_dict['yellow']) 
    GPIO.output(led_pin_dict['blue'], led_state_dict['blue'])
    return redirect(url_for('home'))

if __name__ == "__main__":
   app.run(host='0.0.0.0')