from django.db import models


class Repositorie(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Client(models.Model):
    repositories = models.ManyToManyField(Repositorie)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    repositorie = models.ForeignKey(Repositorie, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Environment(models.Model):
    client = models.ForeignKey(Client, related_name='environments', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
