import requests
import re

openId = ""

baseUrl = "http://qndxx.youth54.cn/SmartLA/dxxjfgl.w"


def study_latest(version):
    """
    学习最新版本
    :param version: 需要学习的大学习版本，注意这个借口只能是最后一个版本
    :return: 接口返回的数据 无误的返回为{"errcode":"0","errmsg":""}

    """

    params = (
        ('method', 'studyLatest'),
    )
    data = {
        'openid': openId,
        'version': version
    }
    response = requests.post(baseUrl, params=params, data=data)
    return response.json()


def study_pastversion(version):
    """
    学习过往版本
    :param version: 需要学习的大学习的版本，这个版本必须是非最后版本，注意与study_latest区分
    :return: 接口返回的数据 无误的返回为{"errcode":"0","errmsg":""}

    """
    params = (
        ('method', 'getLearnPastVersion'),
    )
    data = {
        'openid': openId,
        'version': version
    }
    response = requests.post(baseUrl, params=params, data=data)
    return response.json()


def get_fraction():
    """
    获取分数
    :return: 返回式例{'errcode': '0', 'errmsg': '', 'totalpoints': 28, 'points': 28}

    """
    params = (
        ('method', 'getPerIntegral'),
    )
    data = {
        'openid': openId
    }
    response = requests.post(baseUrl, params=params, data=data)
    return response.json()


def get_past_compilation_list():
    """
    往期大学习的列表

    :return: 很长很长的一个列表

    """
    params = (
        ('method', 'getPastCompilationList'),
    )
    response = requests.post(baseUrl, params=params)
    return response.json()


def get_per_rank():
    """
    获取是否上榜
    (不会吧不会吧，真的有人能上榜？？？)
    :return: {'errcode': '0', 'perrank': '未上榜', 'errmsg': ''}

    """
    params = (
        ('method', 'getPerRank'),
    )
    data = {
        'openid': openId
    }
    response = requests.post(baseUrl, params=params, data=data)
    return response.json()


def get_user_info():
    """
    获取用户基本信息
    :return:

    """
    params = (
        ('method', 'getUserBasicInfo'),
    )
    data = {
        'openid': openId
    }
    response = requests.post(baseUrl, params=params, data=data)
    return response.json()


def get_new_version():
    """
    获取最新一版大学习信息
    :return:
    """
    params = (
        ('method', 'getNewestVersionInfo'),
    )
    data = {
        'openid': openId
    }
    response = requests.post(baseUrl, params=params, data=data)
    return response.json()


def get_phb_pm_date():
    """
    获取排行榜信息
    :return:
    """
    params = (
        ('method', 'getPhbPmDate'),
    )
    data = {
        'flag': '1'
    }
    response = requests.post(baseUrl, params=params, data=data)
    return response.json()


def get_version_under_compilation(hjqc):
    """

    :param hjqc:在获取往期列表中拿到
    :return:
    """
    params = (
        ('method', 'getVersionUnderCompilation'),
    )
    data = {
        'openid': openId,
        'hjqc': hjqc
    }
    response = requests.post(baseUrl, params=params, data=data)
    return response.json()

def get_img_url(url):

    '''
    获取观看完的背景图
    :param url: get_version_under_compilation数组中的获取的url   .get("vds")[0].get("url")
    :return:截图地址
    '''
    id = url.split("/")[-2]
    return "http://h5.cyol.com/special/daxuexi/"+id+"/images/end.jpg"


