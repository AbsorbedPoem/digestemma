import json
import psycopg
from psycopg.rows import dict_row
from meta import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT

# Constantes de conexión

# String de conexión simplificado
DB_CONN_STRING = f"dbname={DB_NAME} user={DB_USER} password={DB_PASS} host={DB_HOST} port={DB_PORT}"

def execute_select_to_json(query: str) -> str:
    """
    Ejecuta una consulta SELECT usando constantes globales 
    y devuelve los resultados serializados en JSON.
    """
    try:
        # Conexión directa usando el string de conexión y el factory de diccionarios
        with psycopg.connect(DB_CONN_STRING, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                results = cur.fetchall()
                
                # 'default=str' previene errores con tipos de datos como datetime o UUID
                return json.dumps(results, indent=2, default=str)
                
    except Exception as e:
        # Retorna el error en formato JSON para mantener consistencia en el tipo de retorno
        return json.dumps({"error": str(e)})

# Uso:
# json_data = execute_select_to_json("SELECT * FROM productos WHERE stock > 0")
# print(json_data)