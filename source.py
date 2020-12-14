#imports - - - - - - -
import atexit, io, sys
import sqlite3
from tabulate import tabulate

#Define Database selection - - - - - -
def select_from_db(stmt, db):
    """ Takes a SQL query and returns results for steel or labor
    """
    conn = sqlite3.connect(db + '.db')
    cur = conn.cursor()
    cur.execute(stmt)
    cols = [i[0] for i in cur.description]
    rows = cur.fetchall()
    conn.close()
    print(tabulate(rows, headers=cols, tablefmt='github'))

#Constructing Steel Database - - - - - - - - - - - - - - - - -
conn = sqlite3.connect('steel.db')
print("Opened database successfully");

conn.execute('''
CREATE TABLE IF NOT EXISTS steel_data([name],
                      [description],
                      [cost]);''')

conn.commit()

print("Table created successfully");

conn.execute("DELETE FROM steel_data")

#Inserting pre defined values
conn.execute("INSERT INTO steel_data VALUES('Pipe - 12in', '12 inch steel galvanized pipe', '550 per ton');")
conn.execute("INSERT INTO steel_data VALUES('Pipe - 6in', '6 inch steel galvanized pipe', '600 per ton');")
conn.execute("INSERT INTO steel_data VALUES('W8', 'Wide Flange Steel beam, 20 ft long', '400 per beam');")
conn.execute("INSERT INTO steel_data VALUES('W10', 'Wide Flange Steel beam, 20 ft long', '500 per beam');")
conn.execute("INSERT INTO steel_data VALUES('W14', 'Wide Flange Steel beam, 20 ft long', '700 per beam');")
conn.execute("INSERT INTO steel_data VALUES('Rebar #3', '3/8 inch diameter', '1575 per ton' );")
conn.execute("INSERT INTO steel_data VALUES('Rebar #4', '0.5 inch diameter', '1600 per ton' );")
conn.execute("INSERT INTO steel_data VALUES('Rebar #5', '5/8 inch diameter', '1675 per ton' );")

conn.commit()

#Constructing Labor Database - - - - - - - - - - - - - - - -
conn = sqlite3.connect('labor.db')
print("Opened database successfully");

conn.execute('''
CREATE TABLE IF NOT EXISTS labor_data([name],
                      [estimated_pay]);''')

conn.commit()

print("Table created successfully");

conn.execute("DELETE FROM labor_data")


#Inserting pre defined values
conn.execute("INSERT INTO labor_data VALUES('Electrician', '20 per hour');")
conn.execute("INSERT INTO labor_data VALUES('Plumber', '20 per hour');")
conn.execute("INSERT INTO labor_data VALUES('Carpenter','20 per hour');")
conn.execute("INSERT INTO labor_data VALUES('Framer', '20 per hour');")
conn.execute("INSERT INTO labor_data VALUES('General Contracter', '20 per hour');")
conn.execute("INSERT INTO labor_data VALUES('Project Manager', '20 per hour' );")
conn.execute("INSERT INTO labor_data VALUES('General Labor', '20 per hour' );")

conn.commit()

#Define Concrete Calculation - - - - - - - - - -
def concrete_calc(area):
  """Returns the subtotal price of concrete needed by the user
  """
  concreteprice = 77 * int(area)
  return concreteprice

#Define Labor Calculation - - - - - - - - -
def labor_calc(rate):
  """Returns the subtotal price of labor needed by the user
  """
  laborprice = rate * (int(length)*168)
  return laborprice

#Define Wood calculation - - - - - - - - - - -
def wood_calc(planks):
  """Returns the subtotal price of wood needed by user
  """
  woodprice = 10 * int(planks)
  return woodprice

    
