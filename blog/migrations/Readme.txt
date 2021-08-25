This is the migrations directory. Dont touch whats in here.
If you want to update anything in migrations you will 
have to modify the models.py file to do so. 

to migrate: 
python manage.py makemigrations
python manage.py sqlmigrate blog 0001     (which is the migration number)
python manage.py makemigrations
python manage.py migrate