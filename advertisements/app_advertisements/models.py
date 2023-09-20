from django.db import models


class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен.')
    create_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    class Meta:
        db_table = 'advertisements'
