from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RoomFeature(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва особливості')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Особливості кімнати"
        verbose_name_plural = "Особливості кімнат"

class Room(models.Model):
    ROOM_TYPES = [('conf', 'Конференц-зал'), ('meet', 'Кімната для зустрічей'), ('work', 'Робоче місце')]
    title = models.CharField(max_length=100, verbose_name='Назва кімнати')
    room_type = models.CharField(max_length=4, choices=ROOM_TYPES, default='meet')
    capacity = models.PositiveIntegerField(verbose_name='Вмістимість осіб')
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = 'Ціна за годину')
    features = models.ManyToManyField(RoomFeature, blank = True, verbose_name='Особливості')
    def __str__(self):
        return f'{self.get_room_type_display()}-{self.title} до {self.capacity} осіб'
    class Meta:
        verbose_name = 'Кімната'
        verbose_name_plural = 'Кімнати'

class Booking(models.Model):
    user = models.ForeignKey(User, en_delete=models.CASCADE, verbose_name='Користувач')
    room = models.ForeignKey(Room, en_delete=models.CASCADE, verbose_name='bookings')
    сustom_name = models.CharField(max_length=100, verbose_name='Ім я замовника')
    custom_email = models.EmailField(verbose_name='почта користувача')
    start_time = models.DateTimeField(verbose_name = 'дата і час спочатку')
    end_time = models.DateTimeField(verbpse_name='дата і час закінчення')
    is_confirmed = models.BooleanField(default=False, verbose_name='підтверджено')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Бронюання {self}: {self.room.title} користувачем {self.custom_name}"
    class Meta:
        verbose_name = 'бронювання'
        verbose_name_plural = 'бронювання'