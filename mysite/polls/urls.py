# URLをViewにマッピングするためのもの
from django.urls import path

from . import views

urlpatterns = [
    # 初期ページのURL
    # views.関数名,nameは、
    # nameは、テンプレートとかから参照するために、短く記載している
    path("",views.index, name="index"),
]
