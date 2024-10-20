from django.http import JsonResponse


class CustomMiddleware:

    def __init__(self,get_response):
        response = self.get_response = get_response  

    def __call__(self,request):
        print("Token",request.META.get('HTTP_AUTHORIZATION'))
        token = request.META.get('HTTP_AUTHORIZATION')
        if(token and len(token.split(" ")) > 1):
            response = self.get_response(request)  
            return response
        else:
            return JsonResponse({
                'message':'Unauthorized'
            },status=401)

      
