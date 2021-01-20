import unittest
import Ya_create_dir
import pytest


class TestYandex:

    def setup(self):
        # Пытался создать пользователя, но не получилось
        user2 = Ya_create_dir.YandexUser(INSERT_TOKEN)
        return user2

    def test_create_dir1(self):
        print('\nСоздание папки')
        user1 = Ya_create_dir.YandexUser(INSERT_TOKEN)  # Вставьте токен
        assert user1.create_dir('New_folder') == 201

    def test_create_dir2(self):
        print('\nПовторное создание папки')
        user1 = Ya_create_dir.YandexUser(INSERT_TOKEN)  # Вставьте токен
        assert user1.create_dir('New_folder') == 409

    def test_create_dir3(self):
        print('\nНезарегистрированный пользователь')
        user1 = Ya_create_dir.YandexUser('135543854684653132121261321561567487486')
        assert user1.create_dir('New_folder') == 401
