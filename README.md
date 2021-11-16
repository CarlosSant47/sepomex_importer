### Read CPM

Con Read Codigo Postal Mexica codigo podras convertir el archivo descargable .txt del catalogo de codigos postales del servicio postal mexicano a un archivo .sql con los inserts requeridos para su importacion en una base de datos de MySQL/MariaDB o tambien insertarlos directamente a tu base de datos (**Nota: el archivo descargado desde el sitio oficial de Correos de Mexico no modificarlo**)
#### Configuracion
Deberas crear un archivo .env con la siguiente configuracion
```txt
DB_HOST=your_server
DB_USER=your_user
DB_PASS=your_pass
DB_NAME=your_dbname
DB_TABLE_INSERT_ZIP_CODES=your_table
```
