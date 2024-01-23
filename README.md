meta: 
-dar um ping no através de uma rota (concluida)

proximos passos:
- criar estrutura pra usuario, treino e exercicio

22/01/2024

__________________________________________________________________________________________________________________________________________
instalar git:
https://www.git-scm.com/download/win
helper:
https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration

command:
git remote add origin https://github.com/juulioclf/backend-academia.git

python:
https://www.python.org/downloads/windows/
v 3.11.7

insomnia (testes):
https://insomnia.rest/download

mysql:
https://dev.mysql.com/downloads/file/?id=526408
__________________________________________________________________________________________________________________________________________


commands:

```
    python -m venv venv

    source venv/Scripts/activate

    pip install -r requirements.txt

    flask run
```

criar arquivo .env com DATABASE_URL = 'mysql+pymysql://seu_usuario:sua_senha@seu_host/sua_base_de_dados'
criar arquivo .flaskenv com FLASK_APP=main:app