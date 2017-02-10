import random
from django.template.loader import render_to_string
from django.utils.encoding import smart_bytes


def readonly_dashboard(application):
    def wrapper(environ, start_response):
        blocked_urls = ['/dashboard', '/profile']
        is_blocked = any(
            [environ.get('PATH_INFO').startswith(url) for url in blocked_urls])
        if is_blocked and environ['REQUEST_METHOD'] == 'POST':
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
