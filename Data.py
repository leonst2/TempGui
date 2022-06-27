import time
import mysql.connector

live_time = []
live_temp = []
live_humidity = []
live_pressure = []

today_time = []
today_temp = []
today_humidity = []
today_pressure = []

hours_time = []
hours_temp = []
hours_humidity = []
hours_pressure = []

week_time = []
week_temp = []
week_humidity = []
week_pressure = []

current_time = []
current_temp = []
current_humidity = []
current_pressure = []

current_x = []
current_y = []

state = 0

print(time.ctime(time.time()), ": Try to connect... ")
db = mysql.connector.connect(
    host="raspberrypi",
    user="root",
    password="tizi",
    database="sensordaten"
)
print(time.ctime(time.time()), ": Successfully connected")
cursor = db.cursor()


def get_state(new_value):
    current_time.clear()
    current_temp.clear()
    current_humidity.clear()
    current_pressure.clear()
    target = new_value
    if target == 0:
        current_time.append(live_time)
        current_temp.append(live_temp)
        current_humidity.append(live_humidity)
        current_pressure.append(live_pressure)
    if target == 1:
        current_time.append(today_time)
        current_temp.append(today_temp)
        current_humidity.append(today_humidity)
        current_pressure.append(today_pressure)
    if target == 2:
        current_time.append(hours_time)
        current_temp.append(hours_temp)
        current_humidity.append(hours_humidity)
        current_pressure.append(hours_pressure)
    if target == 3:
        current_time.append(week_time)
        current_temp.append(week_temp)
        current_humidity.append(week_humidity)
        current_pressure.append(week_pressure)
    print(current_temp)


def get_live_data():
    if len(live_time) > 10:
        live_time.pop(0)
    if len(live_temp) > 10:
        live_temp.pop(0)
    if len(live_humidity) > 10:
        live_humidity.pop(0)
    if len(live_pressure) > 10:
        live_pressure.pop(0)

    print(time.ctime(time.time()), ": Connected cursor")
    db.commit()

    try:
        sql = "SELECT time FROM `sensor01` ORDER BY date DESC, time DESC LIMIT 1"
        cursor.execute(sql)
        res = cursor.fetchall()
        for x in res:
            live_time.append(str(x[0]))

        sql = "SELECT temperature FROM `sensor01` ORDER BY date DESC, time DESC LIMIT 1"
        cursor.execute(sql)
        res = cursor.fetchall()
        for x in res:
            live_temp.append(x[0])

        sql = "SELECT humidity FROM `sensor01` ORDER BY date DESC, time DESC LIMIT 1"
        cursor.execute(sql)
        res = cursor.fetchall()
        for x in res:
            live_humidity.append(x[0])

        sql = "SELECT pressure FROM `sensor01` ORDER BY date DESC, time DESC LIMIT 1"
        cursor.execute(sql)
        res = cursor.fetchall()
        for x in res:
            live_pressure.append(x[0])

        print(time.ctime(time.time()), ": Closed cursor")

    except:
        print(time.ctime(time.time()), ": Not able to connect to Database")


def load_all_data():
    print("loaded all data")
