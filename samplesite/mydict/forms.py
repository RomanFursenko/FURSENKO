from django.views.generic.edit import CreateView #Импортируем форму из фреймворка

from .forms import MdForm

class MdCreateView(CreateView):         #Объявлен новый контроллер-класс
    template_name = 'mydict/create.html'  #Путь к файлу-шаблону создания формы
    form_class = MdForm      #Ссылка на класс формы связаной с моделью
    success_url = '/mydict/'  #Ссылка для перенаправления в случае успеха