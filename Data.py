import time
import mysql.connector

axes_x = []
temp_y = []
humidity_y = []
pressure_y = []

print(time.ctime(time.time()), ": Try to connect... ")
db = mysql.connector.connect(
    host="raspberrypi",
    user="root",
    password="tizi",
    database="sensordaten"
)
print(time.ctime(time.time()), ": Successfully connected")
cursor = db.cursor()


def get_live_data():
    if len(axes_x) > 10:
        axes_x.pop(0)
    if len(temp_y) > 10:
        temp_y.pop(0)
    if len(humidity_y) > 10:
        humidity_y.pop(0)
    if len(pressure_y) > 10:
        pressure_y.pop(0)

    print(time.ctime(time.time()), ": Connected cursor")
    db.commit()

    try:
        sql = "SELECT time FROM `sensor01` ORDER BY `sensor01`.`date` DESC LIMIT 1"
        cursor.execute(sql)
        res = cursor.fetchall()
        for x in res:
            axes_x.append(str(x[0]))

        sql = "SELECT temperature FROM `sensor01` ORDER BY `sensor01`.`date` DESC LIMIT 1"
        cursor.execute(sql)
        res = cursor.fetchall()
        for x in res:
            temp_y.append(x[0])

        sql = "SELECT humidity FROM sensor01"
        cursor.execute(sql)
        res = cursor.fetchall()
        for x in res:
            humidity = x[0]
            humidity_y.append(humidity)

        sql = "SELECT pressure FROM sensor01"
        cursor.execute(sql)
        res = cursor.fetchall()
        for x in res:
            pressure = x[0]
            pressure_y.append(pressure)

        print(time.ctime(time.time()), ": Closed cursor")

    except:
        print(time.ctime(time.time()), ": Not able to connect to Database")

