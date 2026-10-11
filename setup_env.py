"""Configura automaticamente o arquivo .env a partir do .env.example gerando uma SECRET_KEY segura.

Uso:
    uv run python setup_env.py
"""

from pathlib import Path

from django.core.management.utils import get_random_secret_key


def main() -> None:
    env_file = Path(".env")
    example_file = Path(".env.example")

    if env_file.exists():
        print("ℹ️  O arquivo .env já existe. Nenhuma alteração foi feita.")
        return

    if not example_file.exists():
        print("❌ Arquivo .env.example não foi encontrado.")
        return

    content = example_file.read_text(encoding="utf-8")
    new_secret_key = get_random_secret_key()
    new_content = content.replace("sua-secret-key-segura-aqui", new_secret_key)

    env_file.write_text(new_content, encoding="utf-8")
    print(
        "✅ Arquivo .env criado com sucesso com uma SECRET_KEY criptograficamente segura!"
    )


if __name__ == "__main__":
    main()
