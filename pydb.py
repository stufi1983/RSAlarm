import mysql.connector
from mysql.connector import Error

triggerbed = "SELECT * FROM bedevents INNER JOIN bedmap ON bedevents.bed_id = bedmap.bed WHERE status = 'START' AND bed = '"
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='antrianku',
                                         user='root',
                                         password='winda1984')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

#INSERT INTO `bedmap` (`bed`, `room`, `bed_name`, `room_name`, `light_status`) VALUES ('1', '1', 'Satu A', 'Satu', NULL);
#CREATE TABLE bedevents ( id INT PRIMARY KEY, trigger_time DATETIME, bed_id INT NOT NULL, status VARCHAR(5), stop_time DATETIME, CONSTRAINT fk_bed_id FOREIGN KEY (bed_id) REFERENCES bedmap (bed) )
#INSERT INTO `bedevents` (`id`, `trigger_time`, `bed_id`, `status`, `stop_time`) VALUES ('', '2019-08-15 00:00:00', '1', 'START', NULL);

#STATUS
#SELECT room FROM bedevents INNER JOIN bedmap ON bedevents.bed_id = bedmap.bed WHERE status = 'START' GROUP BY room
#SELECT * FROM bedevents INNER JOIN bedmap ON bedevents.bed_id = bedmap.bed WHERE status = 'STOP'

#ADD
#SELECT * FROM bedevents INNER JOIN bedmap ON bedevents.bed_id = bedmap.bed WHERE status = 'START' AND bed = 'XX'
#null so
#INSERT INTO `bedevents` (`id`, `trigger_time`, `bed_id`, `status`, `stop_time`) VALUES ('', '2019-08-15 00:00:00', 'XX', 'START', NULL);

#STOP
#UPDATE `bedevents` SET `status` = 'STOP' WHERE `bedevents`.`bed_id` = 1 AND `status` = 'START'
