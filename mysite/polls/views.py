# Webフレームワークで、ウェブブラウザに
# HTTPレスポンスを返すためのクラスをインポートする
from django.http import HttpResponse

def index(request):
    #HTTPレスポンスを返す
    return HttpResponse("Hello")
