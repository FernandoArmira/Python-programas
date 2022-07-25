import mysql.connector

try:

    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='halo2195', db='python-mysql' )
    cur = miConexion.cursor()

    if miConexion.is_connected:
        print("Conexion a BD correcta")

        cur.execute( "SELECT Nombres, Apellidos FROM nombres" )
        for Nombres, Apellidos in cur.fetchall() :
            print(Nombres, Apellidos)
        

except Exception as ex:
    print(ex)

finally:
    if miConexion.is_connected:
        miConexion.close()