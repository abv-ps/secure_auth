from django.db import connection

def get_user_by_email(email: str):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM accounts_customuser WHERE email = %s", [email])
        return cursor.fetchone()