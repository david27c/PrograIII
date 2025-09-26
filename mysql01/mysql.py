import mysql

class Articulos:
    def abrir(self):
        conexion=(mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="",
                                          database="ugb01")
        return conexion

    def guardar(self, datos):
        cone = self.abrir
        cursor=cone.cursor()
        sql="insert into productos(nombre, precio) values (%s,%s)"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select nombre, precio from productos where codigos=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select nombre, precio from productos=%s"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def baja(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "delete from productos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.rowcount()

    def modificacion(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "update porductos set nombre=%s, precio=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.rowcount()