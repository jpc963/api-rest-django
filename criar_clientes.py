import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from semiauto.models import Cliente


def criando_pessoas(quantidade_de_pessoas):
    fake = Faker("pt_BR")
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        nome = fake.name()
        cpf = CPF()
        cpf = cpf.generate()
        email = "{}@{}".format(nome.lower(), fake.free_email_domain())
        email = email.replace(" ", "")
        telefone = "{} 9{}-{}".format(
            random.randrange(10, 99),
            random.randrange(1000, 9999),
            random.randrange(1000, 9999),
        )
        data_nascimento = '{}-{}-{}'.format(random.randrange(1950, 2005), random.randrange(1, 12),
                                            random.randrange(1, 31))
        p = Cliente(
            nome=nome, cpf=cpf, email=email, telefone=telefone, data_nascimento=data_nascimento)
        p.save()


criando_pessoas(200)
print("Pessoas criadas com sucesso!")
