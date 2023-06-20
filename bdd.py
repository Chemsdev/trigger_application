import mysql.connector


# Fonction permettent de faire la connexion à la base de données.
def connect(host:str, user:str, password:str, database:str):
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return db

from mysql.connector import connect

def requete():
    
    conn = connect(
        host     = "chemsdineserver.mysql.database.azure.com", 
        user     = "chemsdine", 
        password = "Ounissi69800",
        database = "bdd_trigger"
    )
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS `trigger`
        (id INT AUTO_INCREMENT PRIMARY KEY,
        value TEXT)
    ''')
    
    cursor.execute("INSERT INTO `trigger` (value) VALUES ('test_2')")
    conn.commit()
    print("Donnée insérée avec succès !")
        
requete()
