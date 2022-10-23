from rest_framework import permissions, viewsets
from accounts.models import Author
from manuscripts.models import Manuscript
from accounts.models import *
from manuscripts.serializers import ManuscriptSerializer
from rest_framework.response import Response

class ManuscriptViewSet(viewsets.ModelViewSet):
    # import pdb; pdb.set_trace()
    queryset = Manuscript.objects.all()
    serializer_class = ManuscriptSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request):
        # import pdb; pdb.set_trace()
        user=request.user.id
        author=Author.objects.get(user_id=user)

        manuscript=Manuscript.objects.filter(author_id=author.id)
        serializer=ManuscriptSerializer(manuscript,many=True)
        return Response(serializer.data)
