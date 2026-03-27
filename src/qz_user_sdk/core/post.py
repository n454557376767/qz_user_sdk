import httpx
import json
class Post:
    """Post类
    
    Args:
        token: 轻昼token
    """
    def __init__(self,token = ""):
        self.base_url = "https://hehenya.dpdns.org:8505"
        self.token = token        
        self.headers = {
            "Accept-Language": "zh-cn,zh;q=0.5",
            "Accept-Charset": "UTF-8",
            "x-access-token": self.token,
            "Content-Type": "application/json",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }

    def send_message(self, content, category_id, message_type=None, is_markdown=None,title=None):
        """发送帖子
        Args:
            content:帖子内容
            category_id:分区id
            message_type:消息类型,默认None
            is_markdown:是否为markdown,默认None
            title:标题,默认None

        """
        url = f"{self.base_url}/post_message"
        data = {
            "category_id": category_id,
            "content": content
        }
        
        if is_markdown:
            data["is_markdown"] = is_markdown
        if message_type:
            data["message_type"] = message_type
        if title:
            data["title"] = title    
        try:
            response = httpx.post(url, headers=self.headers, data=json.dumps(data))
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"

    def like_message(self, message_id):
        """对帖子实施点赞
        Args:
            message_id:帖子id
        """
        url = f"{self.base_url}/like_message"
        data = {"message_id": message_id}
        
        try:
            response = httpx.post(url, headers=self.headers, data=json.dumps(data))
            return response.json()
        except Exception as e:
            return str(e)

    def get_messages(self, category_id, page, per_page):
        """获取帖子列表
        Args:
            category_id:分区id
            page:页码
            per_page:每页数量
        """
        url = f"{self.base_url}/v3/get_message?category_id={category_id}&page={page}&per_page={per_page}"
        
        try:
            response = httpx.get(url, headers=self.headers)
            return response.json()
        except httpx.RequestException as e:
            return f"请求出错: {str(e)}"
            
    def reply_to_message(self, content, category_id, referenced_message_id):
        """回复消息
        Args:
            content:内容
            category_id:分区id
            referenced_message_id:要回复的帖子id
        """
        url = f"{self.base_url}/post_referenced_message"
        data = {
            "content": content,
            "category_id": category_id,
            "referenced_message_id": referenced_message_id
        }
        
        try:
            response = httpx.post(url, headers=self.headers, data=json.dumps(data))
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"
    