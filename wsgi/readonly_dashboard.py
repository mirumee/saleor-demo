
def readonly_dashboard(application):
    def wrapper(environ, start_response):
        blocked_urls = ['/dashboard', '/profile']
        is_blocked = any(
            [environ.get('PATH_INFO').startswith(url) for url in blocked_urls])
        if is_blocked and environ['REQUEST_METHOD'] == 'POST':
            start_response('204 No Content', [])
            return []
        return application(environ, start_response)
    return wrapper
