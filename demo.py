import index
import time

def get_new_images():

    """
    获取最新版截图
    :return:
    """
    version = index.get_new_version()
    img = index.get_img_url(version.get("dxxurl"))
    print(img)

def get_images(version):
    """
    获取以往版本截图
    :return:
    """
    compilation = index.get_version_under_compilation(version)
    vds = compilation.get("vds")
    for kv in vds:
        url = kv.get("url")
        print(index.get_img_url(url))


def get_all_version():
    '''
    获取所有的id
    :return:
    '''
    number = []
    compilation_list = index.get_past_compilation_list()
    vds = compilation_list.get("vds")
    for key in vds:
        number.append(key.get("xh"))
    return number


def get_all_images():
    '''
    获取所有的图片
    :return:
    '''
    version = get_all_version()
    for key in version:
        get_images(key)


def study_all():
    '''
    学习往期所有大学习
    :return:
    '''
    version = get_all_version()
    for key in version:
        compilation_list = index.get_version_under_compilation(key)
        list_get = compilation_list.get("vds")
        print(list_get)
        for key1 in list_get:
         index.study_pastversion(key1.get("version"))
         time.sleep(10)
         print(key1.get("version"))

study_all()