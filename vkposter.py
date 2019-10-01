#!/usr/bin/env python
# coding: utf-8


class VKPoster:

    def __init__(self):
        self.users = {}
        # raise NotImplementedError

    def user_posted_post(self, user_id: int, post_id: int):
        self.user_sign(user_id)
        self.users[user_id]['posts'] += [post_id]
        pass

    def user_read_post(self, user_id: int, post_id: int):
        self.user_sign(user_id)
        self.users[user_id]['views'] += [post_id]
        pass

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        self.user_sign(follower_user_id)
        self.users[follower_user_id]['follows'] += [followee_user_id]
        pass

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        self.user_sign(user_id)
        newest_posts = []
        new = 0
        for i in range(k):
            self.i = lambda n: self.users[user_id] if self.users[user_id] not in newest_posts
        for i in self.users[user_id]['follows']:
            self.users[i]['posts'].sort()
            newest_posts += self.users[i]['posts'][:k]
        return newest_posts
        pass

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        pass

    def user_sign(self, user_id):
        if self.users.get(user_id) is None:
            self.users[user_id] = {'posts': [], 'views': [], 'follows': []}
        return None


a = VKPoster()
a.user_posted_post(111, 333)
a.user_posted_post(444, 123)
a.user_posted_post(444, 124)
a.user_posted_post(444, 125)
a.user_follow_for(111, 444)
a.user_read_post(111, 555)
print(a.get_recent_posts(111,2))
print(a.users)
