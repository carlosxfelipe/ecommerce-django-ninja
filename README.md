# 🛒 Ecommerce Django Ninja

API moderna para e-commerce construída com **Django**, **Django Ninja** e documentada interativamente via **Scalar**, gerenciada com **uv**.

---

## 📋 Pré-requisitos

- [Python](https://www.python.org/) >= 3.14
- [uv](https://docs.astral.sh/uv/) (gerenciador de pacotes e ambientes Python ultra-rápido)

> Caso ainda não tenha o `uv` instalado:
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

O servidor estará disponível em: `http://localhost:8000`

---

## 🌐 Endpoints Disponíveis

| Recurso | URL | Descrição |
|---|---|---|
| 📖 **API Docs (Scalar)** | [http://localhost:8000/api/docs](http://localhost:8000/api/docs) | Documentação interativa da API |
| 🩺 **Health Check** | [http://localhost:8000/api/health](http://localhost:8000/api/health) | Verificação de status da aplicação |
| 🏓 **Core Ping** | [http://localhost:8000/api/core/ping](http://localhost:8000/api/core/ping) | Endpoint de teste da rota modular `core` |
| 🛠️ **Django Admin** | [http://localhost:8000/admin/](http://localhost:8000/admin/) | Painel administrativo do Django |

> **Dica**: Para acessar o Django Admin, crie um superusuário:
> ```bash
> uv run python manage.py createsuperuser
> ```

---

## 🧹 Qualidade de Código (Ruff)

Formatação e análise estática de código com **Ruff**:

```bash
# Formatar todo o código
uv run ruff format .

# Linter e correções automáticas
uv run ruff check --fix
```

---

## 💡 Criando Novos Apps Modularizados

Para manter a estrutura organizada, os novos apps devem ser criados dentro do diretório `apps/`:

```bash
uv run python manage.py startapp my_app apps/my_app
```

### Passos para registrar o novo app:

1. **Adicionar o app em `config/settings.py`**:
   ```python
   INSTALLED_APPS = [
       ...,
       "apps.my_app",  # ou "my_app" dependendo da configuração de sys.path
   ]
   ```

2. **Criar o router em `apps/my_app/api.py`**:
   ```python
   from ninja import Router

   router = Router(tags=["My App"])


   @router.get("/")
   def list_items(request):
       return {"items": []}
   ```

3. **Registrar o router em `config/api.py`**:
   ```python
   from apps.my_app.api import router as my_app_router

   api.add_router("/my-app", my_app_router)
   ```

---

## 📁 Estrutura do Projeto

```text
ecommerce-django-ninja/
├── apps/               # Aplicações Django modulares
│   ├── __init__.py
│   └── core/           # App principal/exemplo
│       └── api.py
├── config/             # Configurações do projeto Django
│   ├── api.py          # Ponto de entrada do NinjaAPI e rotas
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env.example        # Exemplo de variáveis de ambiente
├── manage.py
├── pyproject.toml      # Configuração de dependências do uv
└── uv.lock             # Lockfile do uv
```
