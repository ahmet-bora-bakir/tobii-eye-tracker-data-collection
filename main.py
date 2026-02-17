import tobii_research as tr
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import cm

left_x = []
left_y = []
right_x = []
right_y = []

time_ = []

def gaze_data_callback(gaze_data):
    gaze_left_eye = gaze_data['left_gaze_point_on_display_area']
    gaze_right_eye = gaze_data['right_gaze_point_on_display_area']
    # Print gaze points of left and right eye
    print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(gaze_left_eye, gaze_right_eye))

    left_x.append(gaze_left_eye[0])
    left_y.append(gaze_left_eye[1])

    right_x.append(gaze_right_eye[0])
    right_y.append(gaze_right_eye[1])

    current_time = time.time()
    time_.append(current_time)
    
    


def choosingDevice(eyeTrackers):
    deviceTag = input("Please input a device parameter(address, model, " \
    "name(it may have some issues), or serial number) to choose which device you are going to use: ")
    for x in eyeTrackers:
        if(deviceTag == x.address or deviceTag == x.model or deviceTag == x.device_name or deviceTag == x.serial_number):
            return x

    print("Device couldn't be founded.")
    return None

print("Searching for eye trackers...")
founded_eyetrackers = np.array(tr.find_all_eyetrackers())

number_of_trackers = len(founded_eyetrackers)

if (number_of_trackers == 0):
    print("Eye trackers couldn't be found.")

elif(number_of_trackers > 0):
    for x in founded_eyetrackers:
     print("Address: " + x.address)
     print("Model: " + x.model)
     print("Name (It's OK if this is empty): " + x.device_name)
     print("Serial number: " + x.serial_number)
    
    mainDevice = choosingDevice(founded_eyetrackers)
    while(mainDevice == None):
       flag = input("To exit without choosing a device type \"exit\": ")
       if(flag == "exit"):
          break
       else:
          mainDevice = choosingDevice(founded_eyetrackers)
    
    if(mainDevice is not None):
        timeInput = input("Please input a time(in seconds) that you want to track: ")
        mainDevice.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
        time.sleep(float(timeInput))
        mainDevice.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)

        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

        ax.scatter(left_x, left_y, time_, color = 'r', label = "left eye", s = 10)
        ax.scatter(right_x, right_y, time_, color = 'b', label = "right eye", s = 10)

        plt.show()

