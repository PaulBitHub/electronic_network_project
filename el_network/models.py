from django.db import models

NULLABLE = {"blank": True, "null": True}


class Supplier(models.Model):
    """
    Класс поставщика с присущими ему полями
    """

    name = models.CharField(max_length=300, verbose_name="Поставщик")
    email = models.EmailField()
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=200, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Класс продукта с присущими ему полями
    """
    name = models.CharField(max_length=300, verbose_name="Продукт")
    model = models.CharField(max_length=300, verbose_name="Модель продукта")
    description = models.CharField(
        max_length=500, verbose_name="Описание продукта", **NULLABLE
    )

    def __str__(self):
        return f"{self.name} {self.model}"


class NetworkNode(models.Model):
    """
    Класс для хранения информации о различных узлах сети, связанных с поставщиками и продуктами
    """

    LEVELS_CHOICES = (
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    )

    name = models.CharField(max_length=300, verbose_name="Название узла")
    level = models.IntegerField(choices=LEVELS_CHOICES, verbose_name="Уровень узла")
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="nodes",
        verbose_name="Поставщик",
    )
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="children",
        verbose_name="Родитель",
    )
    email = models.EmailField(verbose_name="Электронная почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=200, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    debt_to_supplier = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность поставщику",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.get_level_display()}: {self.name}"

    def clean_debt(self):
        """
        Очищает задолженность перед поставщиком
        """
        self.debt_to_supplier = 0.00
        self.save()

    clean_debt.short_description = "Очистить задолженность перед поставщиком"  #текст команды для пользователя

    def save(self, *args, **kwargs):
        if self.parent:
            if self.level <= self.parent.level:
                raise ValueError("Уровень узла должен быть выше, чем у родительского")
        super().save(*args, **kwargs)
