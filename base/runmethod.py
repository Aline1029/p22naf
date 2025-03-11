#coding:utf-8
from util import logger
import requests
import json
class RunMethod:
	def post_main(self,url,data,header=None):
		res = None
		if header !=None:	
			res = requests.post(url=url,data=data,headers=header)
		else:
			res = requests.post(url=url,data=data)
			logger.debug("[DEBUG] 响应状态码:", res.status_code)
			logger.debug("[DEBUG] 响应头:", res.headers)
			logger.debug("[DEBUG] 原始内容:", res.text[:500])  # 截取前500字符
		return res.json()

	def get_main(self,url,data=None,header=None):
		res = None
		if header !=None:	
			res = requests.get(url=url,data=data,headers=header,verify=False)
			logger.debug("[DEBUG] 响应状态码get with head:", res.status_code)
			logger.debug("[DEBUG] 响应头get with head:", res.headers)
			logger.debug("[DEBUG] 原始内容get with head:", res.text[:500])  # 截取前500字符
		else:
			res = requests.get(url=url,data=data,verify=False)
			logger.debug("[DEBUG] 响应状态码:", res.status_code)
			logger.debug("[DEBUG] 响应头:", res.headers)
			logger.debug("[DEBUG] 原始内容:", res.text[:500])  # 截取前500字符
		return res.json()

	def run_main(self,method,url,data=None,header=None):
		res = None
		if method == 'Post':
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		return json.dumps(res,ensure_ascii=False)
		#return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
