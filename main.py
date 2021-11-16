from lib.dotenv.main import dotenv_values
from lib.mysql import connector
import functions
from bcolors import bcolors

CONFIG = dotenv_values('.env')


db = connector.connect (
  host=CONFIG["DB_HOST"],
  user=CONFIG["DB_USER"],
  password=CONFIG["DB_PASS"],
  database=CONFIG["DB_NAME"]
)


headerFields = []
zipFileData = open('CPdescarga.txt', 'r',encoding='ISO-8859-1')
listLines = zipFileData.readlines()
counter = 0
importSQL = open("import.sql", "a+")
for line in listLines:
  dataFields = line.strip().split('|')

  #PRINT MESSAGE FOR CORREOS DE MEXICO
  if len(dataFields) == 1:
    bcolors.print(line.strip(), bcolors.FAIL)

  #SAVE FIELDS COLUMN NAMES
  if counter == 1:
    headerFields = dataFields

  #IN ZIP CODE FILE THE 2 LINE ARRAY EN ABOVE CONTAINS ZIPS CODES
  if counter >= 2:
    importSQL.write(functions.createInsertSentence(CONFIG['DB_TABLE_INSERT_ZIP_CODES'], headerFields, dataFields))
  counter += 1


