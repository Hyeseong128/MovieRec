# Generated by Django 4.2.4 on 2024-11-21 01:26

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
        ('movies', '0001_initial'),
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='사용자의 생년월일', null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='deleted_at',
            field=models.DateTimeField(blank=True, help_text='소프트 삭제된 날짜', null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='favorite_actors',
            field=models.ManyToManyField(blank=True, help_text='사용자가 즐겨찾기한 배우 목록', related_name='favorited_by_users', to='movies.actor'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='favorite_directors',
            field=models.ManyToManyField(blank=True, help_text='사용자가 즐겨찾기한 감독 목록', related_name='favorited_by_users', to='movies.director'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='favorite_genres',
            field=models.ManyToManyField(blank=True, help_text='사용자의 선호 장르 목록', related_name='users', to='movies.genre'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(blank=True, help_text='사용자가 팔로우하는 다른 사용자 목록', related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_phone_verified',
            field=models.BooleanField(default=False, help_text='전화번호 인증 여부'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='liked_movies',
            field=models.ManyToManyField(blank=True, help_text='사용자가 좋아요를 누른 영화 목록', related_name='liked_by_users', to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='liked_posts',
            field=models.ManyToManyField(blank=True, help_text='사용자가 좋아요를 누른 게시글 목록', related_name='liked_by_users', to='community.post'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='liked_reviews',
            field=models.ManyToManyField(blank=True, help_text='사용자가 좋아요를 누른 리뷰 목록', related_name='liked_by_users', to='community.review'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, help_text='사용자의 전화번호', max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, help_text='사용자 프로필 이미지', max_length=300, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='verification_code',
            field=models.IntegerField(blank=True, help_text='전화번호 인증 코드', null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='watched_movies',
            field=models.ManyToManyField(blank=True, help_text='사용자가 시청한 영화 목록', related_name='watched_by_users', to='movies.movie', verbose_name='본 영화 목록'),
        ),
    ]
