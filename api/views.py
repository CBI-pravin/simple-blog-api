from django.shortcuts import render

from rest_framework.views import APIView
from .serializers import MyUserSerializer,loginuserSerializer,BlogSerializer,CommentSerializer
from .models import MyUser,Blog,Comments
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated

class RegisterUserAPI(APIView):
    

    def post(self,request):
        serializer = MyUserSerializer(data = request.data,context = {"author":request.user.email})

        if serializer.is_valid():
            serializer.save()
            user_obj = MyUser.objects.get(email = serializer.data['email'])
            token, created = Token.objects.get_or_create(user=user_obj)
          
            return Response({"status":"success",
                                "details":"account created successfully",'token': token.key,},
                                status=status.HTTP_201_CREATED)       
        else:
            return Response({'status': 'error',
                            "details":serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        
class LoginUserAPI(APIView):
    def post(self, request):
        serializer = loginuserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = MyUser.objects.get(email=email)
            except MyUser.DoesNotExist:
                return Response({'status': 'error',
                                    "details":"can't find user!"},
                                    status=status.HTTP_404_NOT_FOUND)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
               
                return Response({'status': 'success',
                                    "details":"Successfully login!",
                                    "token":token.key},
                                    status=status.HTTP_200_OK)
            else:
                return Response({'status': 'error',
                                    "details":"email or password are not valid !"},
                                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'status': 'error',
                                "details":serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)





class DetailBlogAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # THIS ,ETHOD IS TO GET DETAIL VIEW OF ONE BLOG
    def get(self, request,blog_id):
        try:
            obj = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"status":"error",
                                "details":"Blog not found."},status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(obj)
        return Response(serializer.data)
    

    # THIS METHOD IS TO LIKE POST
    def post(self, request,blog_id):
        try:
            obj = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"status":"error",
                                "details":"Blog not found."},status=status.HTTP_404_NOT_FOUND)
        if request.user not in obj.likes.all():
            obj.likes.add(MyUser.objects.get(email = request.user.email))
        else:
            obj.likes.remove(MyUser.objects.get(email = request.user.email))
        obj.save()
        serializer = BlogSerializer(obj)
        return Response(serializer.data)
    
   
    # THIS METHOD IS TO UPDATE TITLE OR CONTENT OF CURRENT POST 
    def put(self,request,blog_id):
     
        title = request.data['title']
        content = request.data['content']
        try:
            obj = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"status":"error",
                             "details":"Blog not found."},status=status.HTTP_404_NOT_FOUND)
        if obj.author != request.user:
            return Response({"status":"error",
                             "details":"You are not the author."},status=status.HTTP_400_BAD_REQUEST)
        serializer = BlogSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","details":"successfully updated"
                             ,"data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # THIS MEHTOD IS TO DELETE BLOG
    def delete(self,request,blog_id):
        try:
            obj = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"status":"error",
                             "details":"Blog not found."},status=status.HTTP_404_NOT_FOUND)
        if obj.author != request.user:
            return Response({"status":"error",
                             "details":"You are not the author."},status=status.HTTP_400_BAD_REQUEST)
        obj.delete()
        return Response({"status":"success",
                         "details":"successfully deleted post."})
    




class HomeAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # THIS METHOD IS TO SEE ALL BLOGS ORERED BY CREATED DATE
    def get(self,request,):
        try:
            obj = Blog.objects.all().order_by("-published_date")
        except Blog.DoesNotExist:
            return Response({"status":"error",
                                "details":"Blog not found."},status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(obj,many= True)

        return Response(serializer.data)
    
    # THIS METHO IS TO SAVE NEW BLOG
    def post(self, request,):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author = MyUser.objects.get(email= request.user.email))
            return Response({'status': 'success',
                                    "details":"Successfully saved!",
                                    "data":serializer.data
                                    },
                                    status=status.HTTP_200_OK )
        else:
            return Response({'status': 'error',
                                "details":serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)

   



class CommentAPI(APIView):
    """ THIS CLASS IS TO SAVE COMMENTS AND THEIR REPLIES 
        CREATING COMMENT NEED TO MAKE POST METHOD ALONG WITH BLOG ID
        CREATING REPLY TO THAT COMMENT NEED TO PASS REPLY-TO ID OF COMMENT
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # THIS METHOD IS TO GET ALL COMMENTS ORDERED BY CREATED DATE DESCENDING
    def get(self,request,blog_id):
        try:
            obj = Comments.objects.filter(blog = blog_id,is_reply = False).order_by("-created_date")
        except Blog.DoesNotExist:
            return Response({"status":"error",
                                "details":"Blog not found."},status=status.HTTP_404_NOT_FOUND)
        serlializer = CommentSerializer(obj,many= True)

        return Response(serlializer.data)

    # THIS METHOD IS TO SAVE A NEW COMMENT FOR ANY POST 
    def post(self, request, blog_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner = MyUser.objects.get(email =  request.user),
                            blog=Blog.objects.get(id= blog_id ))
            return Response({"status":"success",
                             "details":"successfully saved comment","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error',
                                "details":serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
        
    # THIS METHOD IS TO REPLY A PARTICULAR COMMENT
    def put(self,request,blog_id):
        comment_id = request.data['reply-to']
        try:
            obj = Comments.objects.get(id=comment_id)
        except Comments.DoesNotExist:
            return Response({"status":"error",
                             "details":"Blog not found."},status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer( data=request.data)

        if serializer.is_valid():
            reply =serializer.save(owner = MyUser.objects.get(email =  request.user))
            reply.parent_comment = Comments.objects.get(id = obj.id)
            reply.is_reply = True
            reply.save()
            return Response({"status":"success","details":"successfully updated"
                             ,"data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



class  SearchAPI(APIView):
    def post(self, request):
        keywords = request.data['search'] if request.data['search']!= None else ''
        
        keywords = keywords.split(" ")
        print(keywords)
        result =[]
        for i in keywords:
            if i != "":
                obj= Blog.objects.filter(title__icontains = i).order_by("-published_date")
                serializer = BlogSerializer(obj,many = True)
                for j in serializer.data :
                    if j not in result:
                        result.append(j)
        print(result)
    
        return Response(result)