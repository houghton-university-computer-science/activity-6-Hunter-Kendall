# Activity \#6

### Step 1
Create a django project named ```superdb``` with an app named ```db```.
Add to ```settings.py```:
```
AUTH_USER_MODEL = 'db.User'
```
Also add the ```db``` app to the list of ```INSTALLED_APPS```.

Add to ```admin.py```:
```	
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from courses.models import User

admin.site.register(User, UserAdmin)
```
Add to ```models.py```:
```
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    	pass
```
Run
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
to confirm your site is running.

### Step 2
Create a superuser account in Django by running:
```
python manage.py createsuperuser
```
Run the Django server and confirm that you login with your superuser account at ```http://localhost:8000/admin```.

### Step 3
Below is a UML diagram for a database. <br>
<img src="https://github.com/brandonbate/activity_06/blob/main/uml.png" style="height:50%; width:50%;"/>
<br>
Create this database in Django by modifying ```models.py```. Confirm that it works as expected by logging in at 
```http://localhost:8000/admin```.
Go ahead and create a few entries within the database to see how things work. Try editting and deleting entries as well.

### Step 4
Create a user account that can create orders and order items, but cannot modify any customer or product data. Confirm that the permissions are as expected by logging in with this user at
```http://localhost:8000/admin```.
