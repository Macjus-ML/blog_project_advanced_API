"""
Хорошей практикой является постоянная версионность ваших API
 - v1 /, v2 / и т. д. - поскольку при внесении значительных
  изменений может пройти некоторое время, прежде чем
  различные пользователи API также смогут обновиться.
  Таким образом, вы можете поддерживать API версии v1 в
  течение определенного периода времени, одновременно
  запуская новую обновленную версию v2, и избегать
  поломки других приложений,
  которые зависят от вашего бэкэнда API.
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls # для чтения схемы API
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
# shema_view = get_schema_view(title=API_TITLE)
shema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),  # добавляем версионность
    path('api-auth/', include('rest_framework.urls')),  # добавляем текущего пользователя на Rest API-View
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    # path('schema/', shema_view),
    path('swagger-docs/', shema_view),
]
