import openai
from django.shortcuts import render
from django.conf import settings

#openai.api_key = settings.OPENAI_API_KEY

def chatbot_view(request):
    answer = None
    question = None
    if request.method == "POST":
        question = request.POST.get('question')
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question},
                ],
            )
            answer = response['choices'][0]['message']['content']
        except Exception as e:
            answer = str(e)
    return render(request, 'chatbot/chatbot.html', {'answer': answer, 'question': question})
