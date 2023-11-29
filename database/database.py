import os
import sqlite3


class Database:
    """
    sqlite3 database operation
    """

    def __init__(self, path="./database/sensorData.db"):
        self.path = path
        if not os.path.isfile(path):
            self.create_rangeamp_db()
            self.insert_rangeamp_db(0,0,0)
            self.create_uspadistance_db()
            self.insert_uspadistance_db(0,0,0,0,0,0)
            self.create_uspatime_db()
            self.insert_uspatime_db(0,0,0,0,0,0)

    def create_uspatime_db(self):
        """
        create USPATIME table of database if file not exist.
        :return:
        """
        conn = sqlite3.connect(self.path)
        # no matter the table is exist or not
                     
        # conn.execute("DROP TABLE USPATIME; ")
        conn.execute('''CREATE TABLE IF NOT EXISTS USPATIME
                     (itemid INT  PRIMARY KEY  NOT NULL,
                      time INT,
                      timestamp TEXT,
                      threshold INT,
                      envelope INT,
                      ioline INT); ''')
        conn.commit()
        conn.close()

    def insert_uspatime_db(self, itemid, time, timestamp, threshold, envelope, ioline):
        """_summary_

        Args:
            itemid (_type_): _description_
            time (_type_): _description_
            timestamp (_type_): _description_
            threshold (_type_): _description_
            envelope (_type_): _description_
            ioline (_type_): _description_
        """
        conn = sqlite3.connect(self.path)
        sql = ''' insert into USPATIME
                  (itemid, time, timestamp, threshold, envelope, ioline)
                  values
                  (:itemid, :time, :timestamp, :threshold, :envelope, :ioline)'''

        conn.execute(sql, {'itemid': itemid, 'time': time, 'timestamp': timestamp,
                     'threshold': threshold, 'envelope': envelope, 'ioline': ioline})
        conn.commit()
        conn.close()

    def read_uspatime_db(self):
        """
        read all data from USPATIME table
        :return:
        """
        conn = sqlite3.connect(self.path)
        cursor = conn.execute("SELECT * from USPATIME")
        results = cursor.fetchall()
        conn.close()

        return results

    def read_uspatime_lastid_db(self):
        """
        read the last row id from USPADISTANCE table
        :return:
        """
        conn = sqlite3.connect(self.path)
        cursor = conn.execute(
            "SELECT max(itemid) from USPATIME")
        max_itemid = cursor.fetchone()
        results=max_itemid[0]
        conn.close()
        return results

    def delete_uspatime_db(self):
        """
        delete all data from USPADISTANCE table
        :return:
        """
        conn = sqlite3.connect(self.path)
        conn.execute("DELETE FROM USPATIME")
        conn.commit()
        conn.close()

    def delete_uspatime_t_db(self, timestamp):
        """
        delete sheet
        :param timestamp:
        :return:
        """
        conn = sqlite3.connect(self.path)
        conn.execute("DELETE from USPATIME where timestamp= ?", timestamp)
        conn.commit()
        conn.close()

    def create_uspadistance_db(self):
        """
        create USPADISTANCE table of database if file not exist.
        :return:
        """
        conn = sqlite3.connect(self.path)
        # no matter the table is exist or not
        # conn.execute("DROP TABLE USPADISTANCE; ")
        conn.execute('''CREATE TABLE IF NOT EXISTS USPADISTANCE
                     (itemid INT  PRIMARY KEY  NOT NULL ,
                      distance INT, 
                      timestamp TEXT ,
                      threshold INT,
                      envelope INT,
                      ioline INT);''')
        conn.commit()
        conn.close()

    def insert_uspadistance_db(self,itemid, distance, timestamp, threshold, envelope, ioline):
        """insert new data into USPADISTANCE table of database"""

        conn = sqlite3.connect(self.path)
        sql = ''' insert into USPADISTANCE
                  (itemid, distance, timestamp, threshold, envelope, ioline)
                  values
                  (:itemid, :distance, :timestamp, :threshold, :envelope, :ioline)'''

        conn.execute(sql, {'itemid':itemid, 'distance': distance, 'timestamp': timestamp, 
                     'threshold': threshold, 'envelope': envelope, 'ioline': ioline})
        conn.commit()
        conn.close()


    def read_uspadistance_db(self):
        """
        read all data from USPADISTANCE table
        :return:
        """
        conn = sqlite3.connect(self.path)
        cursor = conn.execute(
            "SELECT * from USPADISTANCE")
        results = cursor.fetchall()
        conn.close()

        return results
    
    def read_uspadistance_lastid_db(self):
        """
        read the last row id from USPADISTANCE table
        :return:
        """
        conn = sqlite3.connect(self.path)
        cursor = conn.execute(
            "SELECT max(itemid) from USPADISTANCE")
        max_itemid = cursor.fetchone()
        results=max_itemid[0]
        conn.close()
        return results

    def delete_uspadistance_db(self):
        """
        delete all data from USPADISTANCE table
        :return:
        """
        conn = sqlite3.connect(self.path)
        conn.execute("DELETE FROM USPADISTANCE")
        conn.commit()
        conn.close()

    def delete_uspadistance_t_db(self, timestamp):
        """
        delete sheet
        :param timestamp:
        :return:
        """
        conn = sqlite3.connect(self.path)
        conn.execute("DELETE from USPADISTANCE where timestamp= ?", timestamp)
        conn.commit()
        conn.close()

    def create_rangeamp_db(self):
        """
        create RANGEAMP table of database if file not exist.
        :return:
        """
        conn = sqlite3.connect(self.path)
        # no matter the table is exist or not
        # conn.execute("DROP TABLE RANGEAMP; ")
        conn.execute('''CREATE TABLE IF NOT EXISTS RANGEAMP
                     (timestamp  INT PRIMARY KEY  NOT NULL,
                      range INT,
                      amplitude INT);''')
        conn.commit()
        conn.close()

    def insert_rangeamp_db(self, timestamp, range, amplitude):
        """insert new data into RANGEAMP table of database

        Args:
            timestamp (_type_): time stemp of the sensor data
            range (_type_): range value
            amplitude (_type_): amplitude value
        """
        conn = sqlite3.connect(self.path)
        sql = ''' insert into RANGEAMP
                  (timestamp, range, amplitude)
                  values
                  (:timestamp, :range, :amplitude)'''

        conn.execute(sql, {'timestamp': timestamp,
                     'range': range, 'amplitude': amplitude})
        conn.commit()
        conn.close()

    def read_rangeamp_db(self):
        """
        read all data from RANGEAMP table
        :return:
        """
        conn = sqlite3.connect(self.path)
        cursor = conn.execute("SELECT * from RANGEAMP")
        results = cursor.fetchall()
        conn.close()

        return results

    def update_rangeamp_db(self, up_key, value, timestamp):
        """
        replace old value to value of up_key (item) depend on switch_id
        :param up_key: the item to be operated
        :param value: new data
        :param timestamp: ids
        :return:
        """
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        if up_key == "range":
            c.execute(
                'UPDATE RANGEAMP set range = ? WHERE timestamp= ?', (value, timestamp))
        elif up_key == "amplitude":
            c.execute(
                'UPDATE RANGEAMP set amplitude = ? WHERE timestamp= ?', (value, timestamp))
        conn.commit()
        conn.close()

    def check_rangeamp_db(self, up_key, timestamp):
        """
        check the value of up_key (item) depend on switch_id
        :param up_key: item
        :param timestamp: ids
        :return:
        """
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        if up_key == "range":
            results = c.execute(
                "SELECT range from RANGEAMP WHERE timestamp= ?",
                timestamp)
        elif up_key == "amplitude":
            results = c.execute(
                "SELECT amplitude from RANGEAMP WHERE timestamp= ?",
                timestamp)
        for row in results:
            print(row)
        conn.close()

    def delete_rangeamp_db(self, timestamp):
        """
        delete sheet
        :param timestamp:
        :return:
        """
        conn = sqlite3.connect(self.path)
        conn.execute("DELETE from RANGEAMP where timestamp= ?", timestamp)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    a = Database(path="database/sensorData.db")
    # a.insert_rangeamp_db("2", "ha", "ga", "ma", "ka", "ta")
    # a.update_rangeamp_db("port_status", "yes", "2")
    results = a.read_uspadistance_db()

    timestamp = [i[0] for i in results]
    # a.delete_rangeamp_db("2")
