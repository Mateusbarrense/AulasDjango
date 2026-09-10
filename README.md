[dontpad.com/PPI-TSI](https://dontpad.com/PPI-TSI)

# 3. Criar e ativar o ambiente virtual
Instale o virtualenv, caso ainda não esteja disponível:

pip install virtualenv
Crie o ambiente virtual:

py -m venv .venv
Ative o ambiente virtual:

.venv\Scripts\activate
Após a ativação, o início da linha de comando deverá apresentar (.venv).

# 4. Instalar o Django
Com o ambiente virtual ativado:

pip install django


# 5. Executar o projeto
Entre na pasta do projeto Django:

cd helloworld
Execute o servidor de desenvolvimento:

py manage.py runserver
Abra o navegador e acesse:

http://localhost:8000