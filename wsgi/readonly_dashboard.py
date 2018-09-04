import random
import re

from django.template.loader import render_to_string
from django.utils.encoding import smart_bytes

BLOCKED_URL = [
    re.compile(r'^/dashboard'),
    re.compile(r'^/([\w-]+/)?account/$')]


def _is_url_blocked(url):
    for pattern in BLOCKED_URL:
        yield pattern.match(url)


def _is_request_blocked(environ):
    is_post = environ['REQUEST_METHOD'] == 'POST'
    request_url = environ['PATH_INFO']
    return is_post and any(_is_url_blocked(request_url))


def readonly_dashboard(application):
    def wrapper(environ, start_response):
        if _is_request_blocked(environ):
            start_response('200 OK', [('Content-Type', 'text/html')])
            image = random.randrange(1, 6)
            ctx = {
                'image_path': 'dashboard/images/pirate-%s.svg' % image,
                'image_class': 'img%s' % image,
                'back_url': environ.get('HTTP_REFERER',
                                        'http://demo.getsaleor.com')}
            page = render_to_string('dashboard/read_only_splash.html', ctx)
            return [smart_bytes(page)]
        return application(environ, start_response)
    return wrapper
