from fastapi import APIRouter
from fastapi import HTTPException, Request, Depends
from schemas.vk import VkResponse, VkResponsePosts
from services.helps.ip_check import rate_limit_client_ip
from services.vk_methods.methods import get_profile, get_post_likes, get_latest_posts


router = APIRouter()


@router.get("/api/v1", response_model=VkResponse | VkResponsePosts)
def api_handler(method: str,
                request: Request,
                limit_client_ip: bool = Depends(rate_limit_client_ip),
                profile: str | None = None,
                link: str | None = None,
                ):
    if method == "profile" and profile:
        data = get_profile(profile)
        return VkResponse(status="success", code=200, data=data.dict())

    elif method == "likes" and link:
        data = get_post_likes(link)
        return VkResponse(status="success", code=200, data=data.dict())

    elif method == "posts" and profile:
        data = get_latest_posts(profile)
        return VkResponsePosts(status="success", code=200, data=data)


    raise HTTPException(status_code=400, detail="Invalid method or profile")
