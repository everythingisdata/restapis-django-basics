from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profileApi import models, permissions, serializers
from rest_framework import filters


class UserProfileViewSet(viewsets.ModelViewSet):
    """Manage Creating and updating the user profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'name',)


class UserLoginApiViews(ObtainAuthToken):
    """Handling creating  user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handling creating, updating and deleting Feeds viewset"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.UpdateOwnStatus
    )
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """Set the user profile to logged user"""

        serializer.save(user_profile=self.request.user)

# class HelloApiView(generics.GenericAPIView):
#     """Test API View"""
#     # serializer_class = serializers.HelloSerializer
#     serializer_classes = serializers.HelloSerializer
#     serializer_class = serializers.HelloSerializer
#
#     def get(self, request, format=None):
#         """Return a list of APIView Features"""
#
#         an_view = [
#             'Uses HTTP methods as function (get, post, delete,put, patch)',
#             'Is similar to traditional DjangoView',
#             'Give you the most  control over you application logic',
#             'Is mapped manually to URLs'
#         ]
#         return Response({'message': 'Hello Django', 'an_view': an_view})
#
#     def post(self, request):
#         """
#         Create hello message with our  name
#          param2 -- A second parameter
#         """
#         serializer = self.serializer_classes(data=request.data)
#
#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'Hello Good Morning! {name}'
#             return Response({'data': message}, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None):
#         """Handling  updating a object"""
#
#         return Response({'method': 'PUT'})
#
#     def patch(self, request, pk=None):
#         """Handling partial update for an object"""
#
#         return Response({'method': 'PATCH'})
#
#     def delete(self, request, pk=None):
#         """Handling partial update for an object"""
#
#         return Response({'method': 'PATCH'})

#
# class HelloViewSets(viewsets.ViewSet):
#     """Test api viewsets"""
#     serializer_class = serializers.HelloSerializer
#
#     def list(self, request):
#         """Return a hello method"""
#         a_viewsets = [
#             'User actions(list, create, retrieve, update, partial_update)',
#             'Automatically maps to urls using Routers',
#             'Provides more functionality with less code ',
#         ]
#
#         return Response({'message': 'Hello world form ViewSets', 'a_viewsets': a_viewsets})
#
#     def create(self, request, pk=None):
#         """Create a hello-world new message"""
#         serializer = self.serializer_class()
#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'Hello world form View set create method for user :{name}'
#             return Response({'message': message})
#         else:
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk=None):
#         """Handling getting an object by Id"""
#
#         return Response({'HTTP_METHOD': 'GET'})
#
#     def update(self, request, pk=None):
#         """Handling updating  an object by Id"""
#
#         return Response({'HTTP_METHOD': 'PUT'})
#
#     def partialupdate(self, request, pk=None):
#         """Handling updating  an object by Id"""
#
#         return Response({'HTTP_METHOD': 'PATCH'})
#
#     def destroy(self, request, pk=None):
#         """Handling Removing and object form Backend """
#
#         return Response({'HTTP_METHOD': 'DELETE'})
