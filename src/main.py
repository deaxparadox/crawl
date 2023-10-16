import asyncio
from tornado.httpclient import AsyncHTTPClient

# class Get(object):
#     def __init__(self):
#         self.__async_http_client = AsyncHTTPClient()

#     def fetch(self) -> 
async def f():
    http_client = AsyncHTTPClient()
    try:
        response = await http_client.fetch("http://www.facebook12131.com")
    except Exception as e:
        print("Error: %s" % e)
    else:
        print(response.body)

if __name__ == "__main__":
    asyncio.run(f())