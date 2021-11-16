def saveDataInDB(database, table, data):
  print()

def exportSQLIntertData(data):
  print()

def createInsertSentence(table, columns, data):
  sqlQuery = "INSERT INTO {}".format(table)
  sqlQuery += "(" + (",".join(["{}"]*len(columns)).format(*columns)) + ")"
  sqlQuery += " VALUES(" + (",".join(["'{}'"]*len(data)).format(*data)) + ");\n"
  return sqlQuery


