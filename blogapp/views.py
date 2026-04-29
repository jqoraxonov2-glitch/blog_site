#class da yozilgan views
from django.shortcuts import get_object_or_404, render
from .models import Post  # DeteilViews bor bu post ustigsa bossa maqolani chiqaradi
from django.views.generic import ListView # djangoda tayyor yaratilgan genereic viewslar M: listviews
# Malumotlarni faqat list sifatida malumot chiqaaradi
#
class PostListView(ListView):
    queryset = Post.published.all() # all hammasini olad va context_object_name =>
    # post sifatida templatega uzatadi
    context_object_name = 'posts' # ctx bu => context_object_name
    paginate_by = 5 # 1ta pageda 5 ta maqol ko'rinsin
    template_name = "blog/post/list.html" # templatega 5 tadan berib turadi

# Post modeldan qidiradi slug=slug ga 1 ta maqolada
# hammasi statusi publish yili oyi teng bo'lganini qaytaradi
def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status="published", publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
# render shortcutdan olinadi       detail.htmlga      # postni tepadagi postga tenglab htmlga beradi











