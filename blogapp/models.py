from django.db import models
from django.contrib.auth.models import User  # djangoning tayyor user modeli bor
# tayyor fieldlarni o'z ichiga oladi
from django.utils import timezone
from django.urls import reverse

# manager bu avval bu ni qonuni asosida malumot uzatiladi
class PublishedManager(models.Manager):
    # get_queryset nomi o'zgarmas qachon get chaqirilsa
    def get_queryset(self):
        # super => Models bu yerda ota class PM ni      # filter query
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = ( # birinchisi draft chornavek chop etilmasdan turadi keyingisi  xotirada saqlaydi
        ('draft', 'Draft'), # chornavek
        ('published', 'Published') # chop etilgani
    )

    title = models.CharField(max_length=255) # sana bir xil turishi uchun
    slug = models.SlugField(max_length=255, unique_for_date="publish") # sarlavha
    # author user ichida gi tayyor fieldga bog'lanyapti  # related bu user ismiga bosilsa uni maqolasi ch\di
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField()    # temi zona bu siz qayerda turib chop etsangiz shu yer ni vaqtini oladi
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # satatus bu
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',) # eng oxirgi yozilgan maqolani birinchiga qo'yadi yani yangisini
# , vergul shart touple qabul qilgani uchun
    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        # reverse urls dan olindi
        return reverse("blog:post_detail", args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug]) #
# rever bu odam kirganda nima chiqishini hal qiladi reverse bajaradi

# posts = Post.objects.filter(status='published')
# p_posts = Post.published.all()




