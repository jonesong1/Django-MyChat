from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Conversation
from .forms import ConversationMessageForm

@login_required
def index(request):
    friends = Conversation.objects.filter(members__in=[request.user.id])
    conversation = None
    # Get the conversation based on the form data
    friend_id = request.GET.get('friend_id')
    if friend_id:
        conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=friend_id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.created_by = request.user
            # Get the conversation ID from the request.POST data
            conversation_id = request.POST.get('conversation_id')
            if conversation_id:
                conversation = Conversation.objects.get(pk=conversation_id)
                conversation_message.conversation = conversation
            
            conversation_message.save()
            conversation.save()
            form = ConversationMessageForm()
    else:
        form = ConversationMessageForm()
    return render(request, 'conversation/index.html', {
        'friends': friends,
        'conversation': conversation,
        'form': form
    })