from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post



class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='giaco', password='pass')

    def test_can_list_posts(self):
        giaco = User.objects.get(username='giaco')
        Post.objects.create(owner=giaco, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data, len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='giaco', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    class PostDetailViewTests(APITestCase):
        def setUp(self):
            giaco = User.objects.create_user(username='giaco', password='pass')
            giaco2 = User.objects.create_user(username='giaco2', password='pass')
            Post.objects.create(owner=giaco, title='a title', content='giaco content')
            Post.objects.create(owner=giaco2, title='some other title', content='giaco2 content')

        def test_can_retrieve_post_using_valid_id(self):
            response = self.client.get('/posts/1/')
            self.assertEqual(response.data['title'], 'a title')
            self.assertEqual(response.status_code, status.HTTP_200_OK)


        def test_user_can_update_own_post(self):
            self.client.login(username='giaco', password='pass')
            response = self.client.put('/posts/1/', {'title': 'a new title'})
            post = Post.objects.filter(pk=1).first()
            self.assertEqual(post.title, 'a new title')
            self.assertEqual(response.status_code, status.HTTP_200_OK)





