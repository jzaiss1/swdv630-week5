# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Week 5 Assignment - Patterns (Facade)

import mysql.connector

class DatabaseFacade():
  def __init__(self, provider=None, dbname=None, host=None, user=None, password=None):
    self.provider = args[0]
    self.dbname = dbname
    self.host = host
    self.user = user
    self.password = password

  def connect(self):
    DBConnection = None
    if self.provider.lower() == 'mysql':
      DBConnection = mysql.connector.connect(host=self.host,
                                             user=self.user,
                                             passwd=self.password,
                                             database=self.dbname)

def main():
  db = DatabaseFacade('mysql', dbname='sales', host="paine.oak.home",user="tommy",)
  connection = db.connect()