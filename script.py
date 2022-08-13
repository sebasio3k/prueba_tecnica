import csv
import django
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prueba.settings")
    django.setup()

    from users.models import Users
    from bienes.models import Bienes


    def create_user():
        name = 'Sebastian'
        username = 'sebasio'
        password = 'test1408'

        try:
            if not Users.objects.filter(username='sebasio'):
                Users.objects.create(
                    name=name,
                    username=username,
                    password=password
                )
                print(f'Usuario creado: username:{username}')

        except Exception as e:
            print(e)


    def populate_table_bienes():
        with open('./data.csv') as file:
            reader = csv.reader(file)
            next(reader)

            Bienes.objects.all().delete()

            for row in reader:
                print(row)
                registro = Bienes(
                    articulo=row[0],
                    descripcion=row[1],
                    usuario=Users.objects.get(pk=1)
                )
                registro.save()


    create_user()
    populate_table_bienes()