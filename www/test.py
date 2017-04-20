# python sss.py
#import sys
import orm, asyncio
from models import User, Blog, Comment

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop, user='root', password='www3111197', db='awesome',host='localhost', port=3306)

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

'''
loop.run_until_complete(test())  
loop.close()  
if loop.is_closed():  
    sys.exit(0)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete( asyncio.wait([test( loop )]) )  
    loop.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
if loop.is_closed():
    sys.exit(0)

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
'''