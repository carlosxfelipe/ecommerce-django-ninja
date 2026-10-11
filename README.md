# 🛒 Ecommerce Django Ninja

API moderna para e-commerce construída com **Django**, **Django Ninja** e documentada interativamente via **Scalar** (com layout clássico), gerenciada com **uv** e **Python 3.14**.

---

## 📋 Pré-requisitos

- [Python](https://www.python.org/) >= 3.14
- [uv](https://docs.astral.sh/uv/) (gerenciador de pacotes e ambientes Python ultra-rápido)

> Caso ainda não tenha o `uv` instalado:
>
> ```bash
> curl -LsSf https://astral.sh/uv/install.sh | sh
> ```

---

## 🚀 Como Clonar e Rodar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/carlosxfelipe/ecommerce-django-ninja.git
cd ecommerce-django-ninja
```

### 2. Sincronizar o ambiente e instalar dependências

```bash
uv sync
```

### 3. Configurar variáveis de ambiente (opcional/recomendado)

```bash
cp .env.example .env
```

### 4. Executar as migrações do banco de dados

```bash
uv run python manage.py migrate
```

### 5. Iniciar o servidor de desenvolvimento

```bash
uv run python manage.py runserver
```

O servidor estará disponível em: `http://localhost:8000/` (ou `http://127.0.0.1:8000/`).

---

## 🌐 Endpoints Disponíveis

| Recurso                  | URL                                                                        | Descrição                                                |
| ------------------------ | -------------------------------------------------------------------------- | -------------------------------------------------------- |
| 📖 **API Docs (Scalar)** | [http://localhost:8000/api/docs](http://localhost:8000/api/docs)           | Documentação interativa da API com layout Scalar Classic |
| 🩺 **Health Check**      | [http://localhost:8000/api/health](http://localhost:8000/api/health)       | Verificação de status e saúde da API                     |
| 🏓 **Core Ping**         | [http://localhost:8000/api/core/ping](http://localhost:8000/api/core/ping) | Endpoint de teste da rota modular `core`                 |
| 🛠️ **Django Admin**      | [http://localhost:8000/admin/](http://localhost:8000/admin/)               | Painel administrativo do Django                          |

> **Dica**: Para acessar o Django Admin, crie um superusuário:
>
> ```bash
> uv run python manage.py createsuperuser
> ```

---

## 🧹 Qualidade de Código (Ruff)

Análise estática e formatação de código com **Ruff**:

```bash
# Formatar todo o código
uv run ruff format .

# Linter e correções automáticas
uv run ruff check --fix .
```

---

## 💡 Criando Novos Apps Modularizados

O projeto utiliza uma arquitetura modular onde os aplicativos residem dentro do diretório `apps/`. Como o diretório `apps/` já está configurado no `sys.path` em `config/settings.py`, os módulos podem ser importados de forma limpa e direta.

### 1. Criar o app dentro de `apps/`

```bash
uv run python manage.py startapp my_app apps/my_app
```

### 2. Registrar o app em `config/settings.py`

Adicione o nome do app diretamente à lista `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    "my_app",  # Import limpo e direto graças à configuração de sys.path
]
```

### 3. Criar as rotas em `apps/my_app/api.py`

```python
from ninja import Router, Schema

router = Router(tags=["My App"])


class ItemSchema(Schema):
    id: int
    name: str
    price: float


@router.get("/", response=list[ItemSchema])
def list_items(request):
    return [
        {"id": 1, "name": "Item 1", "price": 19.99},
    ]
```

### 4. Registrar o router em `config/api.py`

```python
from my_app.api import router as my_app_router

api.add_router("/my-app", my_app_router)
```

O novo endpoint estará imediatamente acessível em `http://localhost:8000/api/my-app/` e catalogado na documentação do Scalar em `/api/docs`.

---

## 📁 Estrutura do Projeto

```text
ecommerce-django-ninja/
├── apps/               # Aplicações Django modulares
│   ├── __init__.py
│   └── core/           # App principal modular
│       └── api.py
├── config/             # Configurações centrais do Django
│   ├── api.py          # Instância do NinjaAPI e registro dos routers
│   ├── asgi.py
│   ├── settings.py     # Configurações do projeto e inclusão de apps no sys.path
│   ├── urls.py         # Rotas principais do projeto
│   └── wsgi.py
├── .env.example        # Modelo de variáveis de ambiente
├── manage.py
├── pyproject.toml      # Gerenciamento de dependências pelo uv
└── uv.lock             # Lockfile determinístico do uv
```
