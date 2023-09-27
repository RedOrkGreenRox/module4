from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен.')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='advertisements/images')

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                f'<span style="color: green; font-weight: bold;">Сегодня в {created_time}</span>'
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                f'<span style="color: gold; font-weight: bold;">Сегодня в {updated_time}</span>'
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")



    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    class Meta:
        db_table = 'advertisements'
