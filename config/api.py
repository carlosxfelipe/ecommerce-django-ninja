from ninja import NinjaAPI
from scalar_ninja import ScalarConfig, ScalarViewer

api = NinjaAPI(
    title="Ninja API",
    version="1.0.0",
    description="API documentation powered by Scalar and Django Ninja",
    docs=ScalarViewer(ScalarConfig(layout="classic")),
)


@api.get("/health", tags=["System"])
def health_check(request):
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "django-ninja",
    }


# Register modular routers
from core.api import router as core_router

api.add_router("/core", core_router)
