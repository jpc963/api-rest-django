import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from faker import Faker
import random
from semiauto.models import Veiculo, Cliente


def criando_veiculos(quantidade_de_veiculos):
    fake = Faker("pt_BR")
    Faker.seed(10)

    for _ in range(quantidade_de_veiculos):
        cliente = Cliente.objects.values_list('id', flat=True)
        cliente = random.choice(cliente)
        modelo = random.choice(
            ['HB20s', '320i', 'S10', 'Civic', 'Golf', 'Argo', 'Uno', 'Gol', 'Celta', 'Onix', 'Astra', 'Cruze',
             'Corolla', 'Focus', 'Fiesta', 'Fusion', 'Ecosport', 'Ka', 'Kwid', 'Sandero', 'Captur', 'Renegade',
             'Compass', 'Toro', 'Tucson', 'HRV', 'Ranger', 'Hilux', 'Strada', 'Duster', 'Logan', 'Doblo', 'Ducato',
             'Jumper', 'Journey', 'Grand Siena', 'Linea', 'Punto', 'Palio', 'Uno', 'Mobi', 'Up', 'Fox', 'Gol',
             'Golf', 'Jetta', 'Passat', 'Tiguan', 'Touareg', 'Amarok', 'Saveiro', 'Spacefox', 'Spacecross',
             'T-Cross', 'Tiguan', 'Touareg', 'Amarok', 'Saveiro', 'Spacefox', 'Spacecross', 'T-Cross', 'Tiguan',
             'Touareg', 'Amarok', 'Saveiro', 'Spacefox', 'Spacecross', 'T-Cross', 'Tiguan', 'Touareg', 'Amarok',
             'Saveiro', 'Spacefox', 'Spacecross', 'T-Cross', 'Tiguan', 'Touareg', 'Amarok', 'Saveiro', 'Spacefox',
             'Spacecross', 'T-Cross', 'Tiguan', 'Touareg', 'Amarok', 'Saveiro', 'Spacefox', 'Spacecross', 'T-Cross',
             'Tiguan', 'Touareg', 'Amarok', 'Saveiro', 'Spacefox', 'Spacecross', 'T-Cross', 'Tiguan', 'Touareg',
             'Amarok', 'Saveiro', 'Spacefox', 'Spacecross', 'T-Cross', 'Tiguan', 'Touareg', 'Amarok', 'Saveiro',
             'Spacefox', 'Spacecross', 'T-Cross', 'Tiguan', 'Touareg', 'Amarok', 'Saveiro', 'Spacefox',
             'Spacecross'])
        placa = fake.license_plate()
        ano = random.randrange(1985, 2023)
        cor = random.choice(['Preto', 'Branco', 'Prata', 'Vermelho', 'Azul', 'Verde', 'Amarelo', 'Cinza', 'Marrom'])
        marca = random.choice(
            ['Volkswagen', 'Fiat', 'Ford', 'Chevrolet', 'Honda', 'Hyundai', 'Renault', 'Toyota'])

        p = Veiculo(
            modelo=modelo, placa=placa, ano=ano, cor=cor, marca=marca, cliente_id=cliente)
        p.save()


criando_veiculos(200)
print("Veiculos criados com sucesso!")
