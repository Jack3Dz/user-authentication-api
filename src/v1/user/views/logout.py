from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


# logout
class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request):
        """
        Remove API Token
        """

        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

