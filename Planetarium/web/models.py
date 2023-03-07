from django.db import models


MATRIX = 9 * '0' + '|' + 11 * '0' + '|' + 12 * '0' + '|' + 11 * '0' + '|' + 7 * '0'


class NewRoomModel(models.Model):
    matrix = MATRIX
    number = models.PositiveIntegerField(
        unique=True,
        null=False,
        blank=False,
    )
    heading = models.CharField(
        max_length=45,
        null=False,
        blank=False
    )
    duration = models.IntegerField(
        null=False,
        blank=False,
    )
    date = models.DateField(
        null=False,
        blank=False,
    )
    time = models.TimeField(
        null=False,
        blank=False,
    )
    seats = models.CharField(
        max_length=1000,
        default=matrix,
    )

    def __str__(self):
        return f'{self.number} {self.heading}'


class Person(models.Model):
    matrix = MATRIX
    name = models.CharField(
        max_length=150,
    )
    for_room = models.ForeignKey(
        NewRoomModel,
        on_delete=models.CASCADE
    )
    seats = models.CharField(
        max_length=1000,
        default=matrix,
    )
