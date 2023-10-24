
# Ecomers 📝

This is a test ecomers application using django web freamework

[![GitHub issues](https://img.shields.io/github/issues/Harijohnson/django-web)](https://github.com/Harijohnson/django-web/issues)
[![GitHub forks](https://img.shields.io/github/forks/Harijohnson/django-web)](https://github.com/Harijohnson/django-web/forks)

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 

## Tech Stack
- **Frontend:** HTML/CSS/javascript
- **Backend:** Django/PostgreSQL


## Quick Start

- Fork and Clone the repository using-
```
git clone https://github.com/Harijohnson/django-web.git
```
- Create a Branch- 
```
git checkout -b <branch_name>
```
- Create virtual environment-
```
python -m venv env
env\Scripts\activate
```
- Install dependencies using-
```
pip install -r requirements.txt
```
*If you have python2 and python3 installed you need to specify python3 by using command:*
```
python3 -m pip install -r requirements.txt
```

- Headover to Project Directory- 
```
cd bloggitt
```
- Make migrations using-
```
python manage.py makemigrations
```
*If you have python2 and python3 installed you need to specify python3 by using command:*
```
python3 manage.py makemigrations
```

- Migrate Database-
```
python manage.py migrate
```
- Create a superuser-
```
python manage.py createsuperuser
```
- Run server using-
```
python manage.py runserver
```
- Push Changes-
```
git add .
git commit -m "<your commit message>"
git push --set-upstream origin <branch_name>
```



## Useful Resources to Learn

- [Django Docs](https://docs.djangoproject.com/en/3.1/)
- [Bootstrap Docs](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
- [Git and GitHub](https://www.digitalocean.com/community/tutorials/how-to-use-git-a-reference-guide)
