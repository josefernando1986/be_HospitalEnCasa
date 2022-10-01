from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer
from hospitalBackend.models.usuario import Usuario

class UsuarioListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = {IsAuthenticated,}

    def list(self, request):
        print("GET a todos los Usuarios")
        queryset = self.get_queryset()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)



class UsuarioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = "id"
    lookup_url_kwarg = 'pk'
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Usuario")
        """
        if a valid data['user_id'] != kwargs['pk']:
        stringResponse = {'detail' : 'Unauthorized Request'}
        return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)    
        """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Usuario")
        """
        if valid_dat['user_id'] != kwargs['pk']:
        stringResponse = {'detail' : 'Unauthorized Request'}
        return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        """
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print("DELETE a Usuario")
        """
        if a valid data['user_id'] != kwargs['pk']:
        stringResponse = {'detail' : 'Unauthorized Request'}
        return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)    
        """
        return super().delete(request, *args, **kwargs)