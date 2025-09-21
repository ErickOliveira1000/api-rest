class Migration(migrations.Migration);

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CeateModel(
            name = 'user',
            fields = [
                ('id'. models.BigAutoField(auto_created=True, primary_Key=True, serialize=True, verbose_name='ID')),
                ('nome', models.CharField(max_lengt=100)),
                ('email', models.EmailField(max_lengt=30)),
                ('cpf', models.CharField(max_lengt=11)),
                ('data_nascimento', models.DateField()),
                ('celular', models.CharField(max_lengt=14)),
            ]
        )
    ]