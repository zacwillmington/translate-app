from rest_framework import viewsets, permissions
from translate.models import Text
from .textSerializers import TextSerializer

# need to import userMetrics class
# current_user should be set along with current_langauge

# Translate Viewset
class TranslateViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    
    permission_classes = [
        permissions.AllowAny,
    ]

    serializer_class = TextSerializer


    #def getUntranslatedText(self, userId, untranslatedTextId=null, textCategory=any):

    def get_texts(self):
        return [];

    # def testTranslatedText(self, userId, translatedText):
    #     query AI endpoing
    #     result = self.sendToAI(translatedText)
    #     self.updateUserMetrics(userId, result)
    #     return JsonResponse(result);

    #def saveTransltedText(self, userId, translatedText):
        #doSave

    #def jsonResponse(self, data, status):