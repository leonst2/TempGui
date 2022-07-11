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

current_today = []
current_hours = []
current_week = []

print(time.ctime(time.time()), ": Try to connect... ")
db = mysql.connector.connect(
    host="91.34.119.145",
    user="root",
    password="root",
    database="temperature_gui"
)
print(time.ctime(time.time()), ": Successfully connected")
cursor = db.cursor()


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
        sql = "SELECT time FROM `sensordaten` ORDER BY date DESC, time DESC LIMIT 1"
        cursor.execute(sql)
        res = cursor.fetchall()
        for x in res:
            print(str(x[0]))
            live_time.append(str(x[0]))

        sql = "SELECT temperature FROM `sensordaten` ORDER BY date DESC, time DESC LIMIT 1"
        cursor.execute(sql)
        res = cursor.fetchall()
        for x in res:
            print(str(x[0]))
            live_temp.append(x[0])

        sql = "SELECT humidity FROM `sensordaten` ORDER BY date DESC, time DESC LIMIT 1"
        cursor.execute(sql)
        res = cursor.fetchall()
        for x in res:
            print(str(x[0]))
            live_humidity.append(x[0])

        sql = "SELECT pressure FROM `sensordaten` ORDER BY date DESC, time DESC LIMIT 1"
        cursor.execute(sql)
        res = cursor.fetchall()
        for x in res:
            print(str(x[0]))
            live_pressure.append(x[0])

        print(time.ctime(time.time()), ": Closed cursor")

    except:
        print(time.ctime(time.time()), ": Not able to connect to Database")


def load_all_data():
    print("loaded all data")


def set_current_data(category):
    current_today.clear()
    current_hours.clear()
    current_week.clear()
    if category == 1:
        current_today.extend(today_temp)
        current_hours.extend(hours_temp)
        current_week.extend(week_temp)
    elif category == 2:
        current_today.extend(today_humidity)
        current_hours.extend(hours_humidity)
        current_week.extend(week_humidity)
    elif category == 3:
        current_today.extend(today_pressure)
        current_hours.extend(hours_pressure)
        current_week.extend(week_pressure)
