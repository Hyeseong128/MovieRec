# Generated by Django 4.2.4 on 2024-11-20 20:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='제목 없음', help_text='리뷰 제목', max_length=255)),
                ('content', models.TextField(help_text='리뷰 내용')),
                ('rating', models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], help_text='별점', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='리뷰 작성 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='리뷰 수정 날짜')),
                ('movie', models.ForeignKey(blank=True, help_text='리뷰 대상 영화', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movie')),
                ('user', models.ForeignKey(help_text='작성자', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='제목 없음', help_text='게시글 제목', max_length=255)),
                ('content', models.TextField(help_text='게시글 내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='게시글 작성 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='게시글 수정 날짜')),
                ('user', models.ForeignKey(help_text='작성자 사용자', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='댓글 내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='댓글 작성 날짜')),
                ('actor', models.ForeignKey(blank=True, help_text='댓글을 작성한 배우', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actor_comments', to='movies.actor')),
                ('director', models.ForeignKey(blank=True, help_text='댓글을 작성한 감독', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director_comments', to='movies.director')),
                ('dislikes', models.ManyToManyField(blank=True, help_text='이 댓글을 싫어요 한 사용자들', related_name='disliked_comments', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, help_text='이 댓글을 좋아요 한 사용자들', related_name='liked_comments', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(blank=True, help_text='댓글을 작성한 영화', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_comments', to='movies.movie')),
                ('parent', models.ForeignKey(blank=True, help_text='대댓글의 부모 댓글', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='community.comment')),
                ('post', models.ForeignKey(blank=True, help_text='댓글을 작성한 게시글', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='community.post')),
                ('review', models.ForeignKey(blank=True, help_text='댓글을 작성한 리뷰', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_comments', to='community.review')),
                ('user', models.ForeignKey(help_text='댓글 작성자', on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['movie', '-created_at'], name='community_r_movie_i_cde40b_idx'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['user', '-created_at'], name='community_r_user_id_0f7d4f_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'movie')},
        ),
    ]
