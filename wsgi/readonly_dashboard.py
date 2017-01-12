
def readonly_dashboard(application):
    def wrapper(environ, start_response):
        dashboard_url = '/dashboard'
        if all((environ.get('PATH_INFO').startswith(dashboard_url),
               environ['REQUEST_METHOD'] == 'POST')):
            start_response('204 No Content', [])
            return []
        return application(environ, start_response)
    return wrapper

