from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from assets.views import CompanyViewSet, EmployeeViewSet, DeviceViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'companies/(?P<company_id>\d+)/employees', EmployeeViewSet, basename='employee')
router.register(r'companies/(?P<company_id>\d+)/devices', DeviceViewSet, basename='device')

schema_view = get_schema_view(
    openapi.Info(
        title="Asset Tracking API",
        default_version='v1',
        description="API for managing assets",
        contact=openapi.Contact(email="your-email@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
