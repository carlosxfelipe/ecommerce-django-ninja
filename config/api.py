from ninja_extra import ControllerBase, NinjaExtraAPI, api_controller
from ninja_extra.permissions import AllowAny
from ninja_jwt.controller import (
    NinjaJWTDefaultController,
    TokenBlackListController,
)
from scalar_ninja import ScalarConfig, ScalarViewer


@api_controller("/token", permissions=[AllowAny], tags=["Token"], auth=None)
class NinjaJWTExtendedController(
    NinjaJWTDefaultController, TokenBlackListController, ControllerBase
):
    """Endpoints completos de JWT: pair, refresh, verify e blacklist (logout)."""

    auto_import = False


api = NinjaExtraAPI(
    title="Ninja API",
    version="1.0.0",
    description="API documentation powered by Scalar and Django Ninja",
    docs=ScalarViewer(ScalarConfig(layout="classic")),
)

# JWT endpoints: /api/token/pair, /api/token/refresh, /api/token/verify, /api/token/blacklist
api.register_controllers(NinjaJWTExtendedController)


@api.get("/health", tags=["System"])
def health_check(request):
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "django-ninja",
    }


# Register modular routers
from accounts.api import router as accounts_router
from core.api import router as core_router

api.add_router("/core", core_router)
api.add_router("/accounts", accounts_router)
