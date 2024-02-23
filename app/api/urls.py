from django.contrib import admin
from django.urls import include, path
from api.apis import QuestionnaireAPIView

# アプリケーションの名前空間
app_name = 'apis'

# 追加
admin.site.site_title = 'shotengai digital twin'
admin.site.site_header = 'shotengai digital twin'
admin.site.index_title = 'questionnaire data'

urlpatterns = [
]
