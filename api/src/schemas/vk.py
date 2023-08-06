from pydantic import BaseModel

class VkProfile(BaseModel):
    profile_id: int
    avatar_url: str
    followers: int
    following: int

class VkPost(BaseModel):
    post_id: str
    url: str
    likes: int
    share: int
    views: int

class VkResponse(BaseModel):
    status: str
    code: int
    data: dict


class VkResponsePosts(BaseModel):
    status: str
    code: int
    data: list[VkPost]







