from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Post, Comment, Expert, Reservation, UserProfile, Payment
from .forms import PostForm, CommentForm
from django.utils import timezone

# Create your views here.

@login_required
def main_view(request):
    return render(request, 'green/main.html')

def community(request):
    posts = Post.objects.all()
    return render(request, 'green/community.html', {'posts': posts})

def mypage(request):
    user = request.user

    context = {
        'username': user.username,
        'full_name': user.get_full_name(),
        'email': user.email,
        'date_joined': user.date_joined,
        'last_login': user.last_login,
    }
    
    return render(request, 'green/mypage.html', context)

def test(request):
    return render(request, 'green/test.html')

def list(request):
    return render(request, 'green/list.html')

def expert(request):
    return render(request, 'green/expert.html')

def market(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    if selected_category:
        products = Product.objects.filter(category_id=selected_category)
    else:
        products = Product.objects.all()
    return render(request, 'green/market.html', {
        'categories': categories,
        'products': products,
    })

def external_redirect_ptech(request):
    return redirect('https://p-techhealth.co.kr/')

def external_redirect_heymoon(request):
    return redirect('https://heymoon.net/shopping')

def external_redirect_jiguhara(request):
    return redirect('https://jiguhara.cafe24.com/')

def external_redirect_puliodays(request):
    return redirect('https://puliodays.com/product/%ED%92%80%EB%A6%AC%EC%98%A4-%EC%A2%85%EC%95%84%EB%A6%AC-%EB%A7%88%EC%82%AC%EC%A7%80%EA%B8%B0-v3/143/')

def external_redirect_costco(request):
    return redirect('https://www.costco.co.kr/BeautyHouseholdPersonal-Care/BathBodyOral-Care/Oral-Care/Red-Seal-Herbal-Toothpaste-110g-x-4/p/634452')

def community_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('green:community')
    else:
        form = PostForm()
    
    return render(request, 'green/community_create.html', {'form': form})

def community_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('green:community_detail', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'green/community_detail.html', {'post': post, 'comments': comments, 'form': form})

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('green:community_detail', post_id=post_id)

def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('green:community_detail', post_id=post.id)
    else:
        form = CommentForm()
    
    return render(request, 'green/add_comment_to_post.html', {'form': form})

def community_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('green:community_detail', post_id=post_id)

    return render(request, 'green/community_detail.html', {'post': post, 'comments': comments, 'form': form})

def community_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('green:community_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'green/community_update.html', {'form': form, 'post': post})

def community_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('green:community')
    
    return render(request, 'green/community_delete.html', {'post': post})

@login_required
def expert(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if not user_profile.is_premium:
            return redirect('green:premium_info')
    except UserProfile.DoesNotExist:
        return redirect('green:premium_info')

    experts = Expert.objects.all()
    return render(request, 'green/expert.html', {'experts': experts})

def reserve(request, expert_id):
    expert = get_object_or_404(Expert, id=expert_id)
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        
        duplicate_reservations = Reservation.objects.filter(
            expert=expert,
            user=request.user,
            date=date,
            time=time
        )
        
        if duplicate_reservations.exists():
            duplicate_reservations.exclude(id=duplicate_reservations.first().id).delete()
        
        if not duplicate_reservations.exists():
            Reservation.objects.create(
                expert=expert,
                date=date,
                time=time,
                user=request.user
            )
        
        return redirect('green:reserve_ok', expert_id=expert.id)
    
    return render(request, 'green/reserve.html', {'expert': expert})

def reserve_ok(request, expert_id):
    expert = get_object_or_404(Expert, id=expert_id)
    return render(request, 'green/reserve_ok.html', {'expert': expert})

def reserve_complete(request, expert_id):
    expert = get_object_or_404(Expert, id=expert_id)
    reservation = Reservation.objects.filter(expert=expert, user=request.user).latest('id')
    return render(request, 'green/reserve_complete.html', {'expert': expert, 'reservation': reservation})

def premium_info(request):
    return render(request, 'green/premium_info.html')

def premium_ok(request):
    if request.method == 'POST':
        return redirect('green:submit_payment')
    return render(request, 'green/premium_ok.html')

def submit_payment(request):
    if request.method == 'POST':
        payment_id = request.POST.get('payment_id', '').strip()
        payment_code = request.POST.get('payment_code', '').strip()
        # 가상 결제 ID : 123456
        if payment_id == '123456' and payment_code == '123456':
            try:
                user_profile, created = UserProfile.objects.get_or_create(user=request.user)
                user_profile.is_premium = True
                user_profile.save()
                return redirect('green:premium_complete')
            except Exception as e:
                print(f"Error: {e}")
                return redirect('green:premium_payment_error')
        else:
            return redirect('green:premium_payment_error')

    return render(request, 'green/submit_payment.html')

def premium_complete(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_profile.is_premium = True
    user_profile.save()
    return render(request, 'green/premium_complete.html')

def premium_payment_error(request):
    return render(request, 'green/premium_payment_error.html')

def liked_posts(request):
    user = request.user
    posts = Post.objects.filter(likes=user)
    return render(request, 'green/liked_posts.html', {'posts': posts})

def authored_posts(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    return render(request, 'green/authored_posts.html', {'posts': posts})

def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'green/reservation_list.html', {'reservations': reservations})
