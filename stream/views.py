from django.shortcuts import render, redirect, get_object_or_404
from .models import Group, VideoLink

def index(request):
    groups = Group.objects.all()
    return render(request, 'stream/index.html', {'groups': groups})

def create_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group')
        Group.objects.create(name=group_name)
        return redirect('index')
    return render(request, 'stream/create_group.html')

def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        video_url = request.POST.get('url')
        VideoLink.objects.create(url=video_url, group=group)
    return render(request, 'stream/group_detail.html', {'group': group})

def delete_video(request, video_id):
    video = VideoLink.objects.get(id=video_id)
    video.delete()
    return redirect('group_detail', group_id=video.group.id)
