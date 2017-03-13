#Python modules ================================================================
import sqlite3                      #SQLite database module
import time                         #Time module
import datetime                     #Datetime module
import random                       #Random number generator module

#Third party modules ===========================================================
#MatPlotLib -----------------------------------------------------------------
    #Source:http://matplotlib.org/
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

#SQLite db function ============================================================
conn = sqlite3.connect('Test.db')   #Connect to a database and/or created it
c = conn.cursor()                   #Defining a db cursor

#Create a table with columns ------------------------------------------------
def Tb_create():                 #Create a table in Test.db
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(\
    unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
        #Table name:    stuffToPlot
        #SQLite cmd:    'CREATE TABLE IF NOT EXISTS'
        #SQLITE columns types:    REAL, TEXT
        #SQLite columns names:    unix, datestamp, keyword, value
        #SQLite cmd is not case sensitive! but it lets the reader know its a db cmd
        #Remeber that the data type and number of chr in the table determinants it size

#Write values and strings to the table in db --------------------------------
def Tb_entry():                     #Write data to table in SQLite db
    c.execute("INSERT INTO stuffToPlot VALUES(124, '12-03-2017', 'Python', 51)")
        #Insert data to all colums in a new row
    conn.commit()   #Save the inserted data to the table
    #c.close()       #Close the cursor in the SQLite db
    #conn.close()    #Close the connection to the SQLite db

#Write variables to the table in db -----------------------------------------
def dynamic_data_entry():           #Write variables to the table of db
    unix = time.time()              #Get current time stamp
    data = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)   #Create a random number between 0 and 10
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value)\
    VALUES (?, ?, ?, ?)", (unix, data, keyword, value))
    conn.commit()
        #The order the columns is insert into the table do not matter
        #All columns in the row must be present when insert data, to
        #skip a column by leaveing a column blank in insert: (unix, datestamp, , vale)

#Read selected data for the table in db -------------------------------------
def Tb_read():
    #Cursor selecting-----------------------------------------------------
    #c.execute("SELECT * FROM stuffToPlot")     #All data in the table
    #c.execute("SELECT * FROM stuffToPlot WHERE value >=3 AND keyword ='Python'")
    c.execute("SELECT keyword, value, datestamp FROM stuffToPlot") #select columns and order
        #Where = search filters
        # (*) stand for (all)
        #data = c.fetchall()     #Fetch all selected
        #data = c.fetchone()     #Fetch one selected row
        #print(data)             #Print all data in table on one line
    #Fetch all selected data ---------------------------------------------
    for row in c.fetchall():    #fetchall do not hold data after used!
        print(row)              #Print each row in the table
        #print(row[0])          #Print only the first column

#Update data in the table ---------------------------------------------------
def Tb_update(old, new):
    #Update table --------------------------------------------------------
    #c.execute("UPDATE stuffToPlot SET value=1 WHERE value=7")              #No variable input
    c.execute("UPDATE stuffToPlot SET value=? WHERE value=?", (old, new))   #Variable input
    conn.commit()
    print 'Updated table: \n', read_from_db()

#Delete data in the table ---------------------------------------------------
def Tb_delete(number, limit):
    #Check number of target rows -----------------------------------------
    c.execute("SELECT * FROM stuffToPlot WHERE value =?", (number,))    #Select target rows
    if(len(c.fetchall()) <=  limit):    #Limited deleting mistakes!
    #Delete from table----------------------------------------------------
        #c.execute('DELETE FROM stuffToPlot WHERE value =99')           #No variable input
        c.execute("DELETE FROM stuffToPlot WHERE value =?", (number,))  #Variable input
        conn.commit()
    #Print response ------------------------------------------------------
        print 'Deleting successfully'
        c.execute("SELECT * FROM stuffToPlot")
        for row in c.fetchall():
            print(row)
    else:
        print 'To many row are selected'

#MatPlotLib function ===========================================================
def graph_data():            #Plot a graph from data in table
    c.execute("SELECT unix, value FROM stuffToPlot")
    dates = []
    values = []
    for row in c.fetchall():
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    else:
        plt.plot_date(dates, values, '-')
        plt.show()

#Function calls ================================================================
Tb_create()                 #Create a table
#Tb_entry()                 #Input data to the table in db
Tb_read()                   #Read values in table from db
#Tb_update(1,7)             #(Old value, new value)
#Tb_delete(6,3)             #(Value to delet, row limit)
graph_data()               #Plot graph from values in table

#Dynamic_data_entry ---------------------------------------------------------
"""for i in range(10): #Create 10 rows in the table with data
    dynamic_data_entry()
    time.sleep(1)   #Sleep for 1 second to see a new time stamp in db!"""

#End program ===================================================================
c.close()
conn.close()
