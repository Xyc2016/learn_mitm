import mitmproxy.script

MEIZHE_HOST = 'meizhe.meideng.net'
STAFF_HOST = 'staff.meideng.net'
MSHOW_HOST = 'meizhe.play.m.jaeapp.com'
KS_HOST = 'ks.meideng.net'
DOUDIAN_HOST = 'doudian.meideng.net'
WX_HOST = 'wx.meideng.net'
TEST_HOST = '127.0.0.1'

QQ_HOST = "www.qq.com"
BAIDU_HOST = "www.baidu.com"

@mitmproxy.script.concurrent
def request(flow):
    print('......')
    r = flow.request
    # 必须先设置 host 再改写 header, 不然会被覆盖
    host = r.headers.get('Host', '')
    authority = r.headers.get(':authority', '')

    # 美折
    if host == QQ_HOST:
        (r.scheme, r.host) = ('http', BAIDU_HOST)
        return
