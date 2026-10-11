"""Cria (ou atualiza) um superusuário de desenvolvimento.

Uso:
    uv run python create_superuser.py

Valores podem ser sobrescritos por variáveis de ambiente:
    SUPERUSER_EMAIL=outro@exemplo.com SUPERUSER_PASSWORD=outra uv run python create_superuser.py
"""

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from accounts.models import User

EMAIL = os.environ.get("SUPERUSER_EMAIL", "carlosxfelipe@gmail.com")
PASSWORD = os.environ.get("SUPERUSER_PASSWORD", "jiraiya123")


def main() -> None:
    user = User.objects.filter(email__iexact=EMAIL).first()

    if user is None:
        User.objects.create_superuser(email=EMAIL, password=PASSWORD)
        print(f"✅ Superusuário criado: {EMAIL}")
        return

    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.set_password(PASSWORD)
    user.save()
    print(
        f"♻️  Usuário já existia; promovido a superusuário e senha redefinida: {EMAIL}"
    )


if __name__ == "__main__":
    main()
