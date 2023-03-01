import ssl

def start():
    # 短信应用SDK AppID
    appid = "1400776865"   # SDK AppID是1400开头
    # 短信应用SDK AppKey
    appkey = "11db1a2356a6368d708cd6c1f574e6ea"
    # 需要发送短信的手机号码
    phone_numbers = ["13538898378"]
    # 短信模板ID，需要在短信应用中申请
    template_id = "" #在模板列表里获取
    # 签名
    sms_sign = "这是签名"

    from qcloudsms_py import SmsSingleSender
    from  qcloudsms_py.httpclient import HTTPError

    ssl._create_default_https_context = ssl._create_unverified_context

    ssender = SmsSingleSender(appid, appkey)
    params = ["6666", "5"]  # 当模板没有参数时，`params = []`
    try:
        # result = ssender.send_with_param(86, phone_numbers[0], template_id,
        #                                  params, sign=sms_sign, extend="", ext="")  # 签名参数不允许为空串
        result = ssender.send_with_param(86, phone_numbers[0], template_id, params, sign=sms_sign)
        print(result)
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)
