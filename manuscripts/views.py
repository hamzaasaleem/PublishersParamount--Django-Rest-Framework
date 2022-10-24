from rest_framework import permissions, viewsets
from accounts.models import Author
from manuscripts.models import Manuscript
from accounts.models import *
from manuscripts.serializers import ManuscriptSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class ManuscriptViewSet(viewsets.ModelViewSet):
    # import pdb; pdb.set_trace()
    queryset = Manuscript.objects.all()
    serializer_class = ManuscriptSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def list(self, request):
        # import pdb; pdb.set_trace()
        user = request.user.id
        author = Author.objects.get(user_id=user)

        manuscript = Manuscript.objects.filter(author_id=author.id)
        serializer = ManuscriptSerializer(manuscript, many=True)
        return Response(serializer.data)

    def create(self, request):

        author = Author.objects.get(user_id=request.data['author'])

        request.data['author']=author.id



        serializer = ManuscriptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        manuscript = Manuscript.objects.get(id=pk)
        data = request.data

        serializer = ManuscriptSerializer(manuscript, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "Status Updated"}
            )
