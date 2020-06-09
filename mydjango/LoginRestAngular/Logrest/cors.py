from django.response import respose
class CorsMiddleware(object):
    def process_response(self,req,resp):
        respose["Access-Control-Allow-Origin"]='*'
        return respose