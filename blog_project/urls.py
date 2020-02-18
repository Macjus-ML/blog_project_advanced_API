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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),  # добавляем версионность
    path('api-auth/', include('rest_framework.urls')),  # добавляем текущего пользователя на Rest API-View
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
]
