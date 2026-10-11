from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from ninja import Router, Schema
from ninja.errors import HttpError
from ninja_jwt.authentication import JWTAuth
from pydantic import EmailStr

User = get_user_model()

router = Router(tags=["Accounts"])


class RegisterIn(Schema):
    email: EmailStr
    password: str
    first_name: str = ""
    last_name: str = ""


class UserOut(Schema):
    id: int
    email: str
    first_name: str
    last_name: str


@router.post("/register", response={201: UserOut})
def register(request, payload: RegisterIn):
    """Cria uma nova conta de usuário com e-mail e senha."""
    email = payload.email.lower()

    if User.objects.filter(email__iexact=email).exists():
        raise HttpError(409, "Já existe uma conta com este e-mail.")

    try:
        validate_password(payload.password)
    except ValidationError as exc:
        raise HttpError(422, " ".join(exc.messages))

    user = User.objects.create_user(
        email=email,
        password=payload.password,
        first_name=payload.first_name,
        last_name=payload.last_name,
    )
    return 201, user


@router.get("/me", response=UserOut, auth=JWTAuth())
def me(request):
    """Retorna os dados do usuário autenticado."""
    return request.auth
