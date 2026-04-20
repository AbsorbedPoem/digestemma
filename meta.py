import os
from dotenv import load_dotenv

env = load_dotenv('.env')

if env:
    model = 'qwen3.5-reviews'
    assitant_host = os.getenv('ASSISTANT_HOST')
    model_host = os.getenv('MODEL_HOST')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
else:
    print("Error: No se pudo encontrar el archivo .env")
    exit()

