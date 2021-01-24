import pyrow
import time


def just_row():
    ergs = list(pyrow.find())
    while len(ergs) == 0:
        ergs = list(pyrow.find())
    erg = pyrow.pyrow(ergs[0])
    print "Connected to erg."

    workout = erg.get_workout()
    print "Waiting for workout to start ..."
    while workout['state'] == 0:
        time.sleep(1)
        workout = erg.get_workout()
    print "Workout has begun"

    while workout['state'] == 1:
        pace_input = erg.send(['CSAFE_GETPACE_CMD', ])
        pace_output = "Stroke Pace = " + str(pace_input['CSAFE_GETPACE_CMD'][0] / 2)

        duration_input = erg.send(['CSAFE_PM_GET_WORKTIME', ])
        duration_output = "Duration = " + str(duration_input['CSAFE_PM_GET_WORKTIME'][0])

        distance_input = erg.send(['CSAFE_GETHORIZONTAL_CMD', ])
        distance_output = "Distance = " + str(distance_input['CSAFE_GETHORIZONTAL_CMD'][0])

        power_input = erg.send(['CSAFE_GETPOWER_CMD', ])
        power_output = "Power = " + str(power_input['CSAFE_GETPOWER_CMD'][0])

        calories_input = erg.send(['CSAFE_GETCALORIES_CMD', ])
        calories_output = "Calories = " + str(calories_input['CSAFE_GETCALORIES_CMD'][0])

        heartrate_input = erg.send(['CSAFE_GETHRCUR_CMD', ])
        heartrate_output = "Heart Rate = " + str(heartrate_input['CSAFE_GETHRCUR_CMD'][0])

        cadence_input = erg.send(['CSAFE_GETCADENCE_CMD', ])
        cadence_output = "Cadence = " + str(cadence_input['CSAFE_GETCADENCE_CMD'][0])

        print (pace_output, duration_output, distance_output, power_output, calories_output, heartrate_output, cadence_output)


just_row()