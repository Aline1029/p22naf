# coding:utf-8
from util import logger
import requests
import json
from util.operation_json import OperetionJson


class OperationHeader:

    def __init__(self, response):
        '''
        self.response = json.loads(response)
        '''



    def get_response_url(self):
        '''
        获取登录返回的token的url
        '''
        url = "http://10.20.46.217:8088/g/hsxone.omc/v/submitLogin"
        return url

    def get_cookie(self):
        '''
        获取cookie的jar文件
        '''
        data={

        }
        url = self.get_response_url()
        opjson = OperetionJson()
        response=requests.post(url,opjson.get_data('user'))
        logger.debug("response",response)
        cookie = response.cookies
        logger.debug("COOKIE",cookie)
        return cookie


    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        logger.debug("COOKIE",cookie)
        op_json = OperetionJson()
        op_json.write_data(cookie)




if __name__ == '__main__':

    logger.basicConfig(level=logger.DEBUG)  # 显示所有HTTP请求细节

    url = "http://10.20.46.217:8088/g/hsxone.omc/v/submitLogin"
    headers = {'Content-Type': 'application/json'}
    data = {
        "operator_code": "378F8B35904CF45EE61FBAB59AE66DCA",
        "password": "35F9954664545A6F",
        "verify": "",
        "referer": "http://10.20.46.217:8088/frame-layout/login"
    }

