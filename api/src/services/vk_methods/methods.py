import os

import vk_api
from fastapi import HTTPException
from schemas.vk import VkProfile, VkPost

VK_TOKEN = os.getenv('VK_TOKEN')


def get_profile(username: str):
    try:
        session = vk_api.VkApi(token=VK_TOKEN)
        vk = session.get_api()
        user_info = vk.users.get(screen_name=username, fields='photo_200, followers_count, counters')[0]

        return VkProfile(
            profile_id=user_info['id'],
            avatar_url=user_info['photo_200'],
            followers=user_info['followers_count'],
            following=user_info['counters'].get('friends', 0)
        )
    except vk_api.exceptions.ApiError as e:
        raise HTTPException(status_code=403, detail="Invalid account name")


def get_post_likes(post_url: str):
    try:
        session = vk_api.VkApi(token=VK_TOKEN)
        vk = session.get_api()

        post_id = post_url.split("wall")[1]
        post_data = vk.wall.getById(posts=post_id)

        likes = post_data[0]['likes']['count']
        shares = post_data[0]['reposts']['count']
        views = post_data[0]['views']['count']

        return VkPost(
            post_id=post_id,
            url=post_url,
            likes=likes,
            share=shares,
            views=views
        )
    except vk_api.exceptions.ApiError as e:
        raise HTTPException(status_code=403, detail="Invalid post URL")


def get_latest_posts(username: str):
    try:
        session = vk_api.VkApi(token=VK_TOKEN)
        vk = session.get_api()
        posts = vk.wall.get(domain=username, count=10)['items']

        latest_posts = []
        for post in posts:
            post_id = str(post['id'])
            post_url = f"https://vk.com/wall{post['owner_id']}_{post_id}"
            likes = post['likes']['count']
            shares = post['reposts']['count']
            views = post['views']['count']
            latest_posts.append(VkPost(post_id=post_id, url=post_url, likes=likes, share=shares, views=views))

        return latest_posts
    except vk_api.exceptions.ApiError as e:
        raise HTTPException(status_code=403, detail="Invalid account name")
