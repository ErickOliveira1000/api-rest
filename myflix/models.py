from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(blank=False, max_length = 30)
    cpf = models.CharField(max_length = 11)
    data_nascimento = models.DataField()
    celular = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome


class stream(models.Model):
    CATEGORIA = (
    ('F', 'Filme'),
    ('S', 'Série'),
    ('D', 'Documentário')
    )
    codigo = models.CharField(max_lengt=10)
    descricao = models.CharField(max_lengt=100, blank=False)
    categoria = models.CharField(max_length=1, choices=CATEGORIA, blank=False, defalte='F')

    def __str__(self):
        return self.codigo