from dotenv import load_dotenv

#carregar arquivo .env
load_dotenv()

#Importar 'os' para ler arquivo
import os

#transferência das informações do .env para variáveis
host1 = os.environ["host"]
user1 = os.environ["user"]
password1 = os.environ ["password"]

