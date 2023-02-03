## Gerador de veículos e clientes para uma concessionária feito  no Django API Rest

### Instalação

1. Crie um ambiente virtual
2. Ative o ambiente virtual
3. Instale as dependências

```bash
- py -m venv env
- env\Scripts\activate
- pip install -r requirements.txt
```

4. Crie o banco de dados: 

```bash	
- python manage.py makemigrations
- python manage.py migrate
```

5. Crie um super usuário: `python manage.py createsuperuser`
6. Inicie o servidor: `python manage.py runserver`

## Modo de uso

Após instalar as dependências, execute os comandos abaixo para criar os veículos e clientes:

- py criar_clientes.py
- py criar_veiculos.py
