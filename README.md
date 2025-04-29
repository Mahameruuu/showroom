1. Clone repositori:

```
git clone https://github.com/username/nama-repo.git
cd nama-repo
```

2. Buat virtual environment (opsional tapi disarankan):

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
   
4. Install dependencies:

```
  pip install -r requirements.txt
```
   
6. Jalankan migrasi database:

```
python manage.py migrate
```
   
9. Jalankan server

```
  python manage.py runserver
```

10. Buka di browser:
```
http://127.0.0.1:8000/
```
