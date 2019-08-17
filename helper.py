from functools import wraps

from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest
from django.views.generic import View

def ajax_required(f):

    @wraps(f)
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest("Not ajax request!")
        return f(request, *args, **kwargs)
    return wrap


class AuthorRequiredMixin(View):

    def dispatch(self, request, *args, **kwargs):
        # 状态和文章实例有user属性
        if self.get_object().user.username != self.request.user.username:
            raise PermissionDenied
        return super(AuthorRequiredMixin, self).dispatch(request, *args, **kwargs)