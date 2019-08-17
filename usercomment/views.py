from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DeleteView

from django_auth_example.helper import ajax_required
from django_auth_example.usercomment.models import News

class NewsListView(LoginRequiredMixin, ListView):
    """首页动态"""
    model = News
    paginate_by = 20
    template_name = 'news/homepage_comment.html'

    def get_queryset(self, **kwargs):
        return News.objects.filter(reply=False).select_related('user', 'parent').prefetch_related('liked')

def post_news(request):
    """发送动态，AJAX POST请求"""
    post = request.POST['post'].strip()
    if post:
        posted = News.objects.create(user=request.user, content=post)
        html = render_to_string('news/news_without_comment.html', {'news': posted, 'request': request})
        return HttpResponse(html)
    else:
        return HttpResponseBadRequest("The content cannot be empty!!")

@login_required
@ajax_required
@require_http_methods(["GET"])
def get_thread(request):
    """返回动态的评论，AJAX GET请求"""
    news_id = request.GET['news']
    news = News.objects.select_related('user').get(pk=news_id)  # 不是.get(pk=news_id).select_related('user')
    # render_to_string()表示加载模板，填充数据，返回字符串
    news_html = render_to_string("news/news_without_comment.html", {"news": news})  # 没有评论的时候
    thread_html = render_to_string("news/news_with_comment.html", {"thread": news.get_thread()})  # 有评论的时候
    return JsonResponse({
        "uuid": news_id,
        "news": news_html,
        "thread": thread_html,
    })

@login_required
@ajax_required
@require_http_methods(["POST"])
def post_comment(request):
    """评论，AJAX POST请求"""
    post = request.POST['reply'].strip()
    parent_id = request.POST['parent']
    parent = News.objects.get(pk=parent_id)
    if post:
        parent.reply_this(request.user, post)
        return JsonResponse({'comments': parent.comment_count()})
    else:  # 评论为空返回400.html
        return HttpResponseBadRequest("The content cannot be empty!!")

@login_required
@ajax_required
@require_http_methods(["POST"])
def post_comment(request):
    """评论，AJAX POST请求"""
    post = request.POST['reply'].strip()
    parent_id = request.POST['parent']
    parent = News.objects.get(pk=parent_id)
    if post:
        parent.reply_this(request.user, post)
        return JsonResponse({'comments': parent.comment_count()})
    else:  # 评论为空返回400.html
        return HttpResponseBadRequest("The content cannot be empty!!")
