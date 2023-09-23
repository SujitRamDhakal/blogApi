from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
# Create your tests here.


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(self):
        testUser = User.objects.create_user(username='abcd', password='123')
        testUser.save()
        testPost = Post.objects.create(
            author=testUser, title='django', body='django framework...')
        testPost.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'abcd')
        self.assertEqual(title, 'django')
        self.assertEqual(body, 'django framework...')
