#coding:utf-8
# import sys
# sys.path.append('G:/inter')
from util.operation_excel import OperationExcel
from util.opea_case_excel import OperaCaseExcel
import json
import os

class OperationJson(object):
	#获取测试ExcelName
	# file_name = OperaCaseExcel()
	#在Excel表中获取json文件
	# test_record = xlrd.open_workbook('../data_config/TestRecordExcel/test.xlsx')
	# 
	

	def __init__(self,json_files = None):
		#获取json文件名
		oc = OperaCaseExcel()
		res = oc.get_case_excel_name()
		json_files = res[1]
		if json_files:
			self.json_files = '../data_config/'+ json_files
		else:
			self.json_files = '../data_config/interface.json'

		self.get_json_data = self.get_json()

	#获取json文件
	def get_json(self):
		with open(self.json_files,encoding = "utf-8") as json_file:
			json_data = json.load(json_file)
		return json_data

	#获取json数据
	def get_data(self,json_id = None):
		if json_id:
			return self.get_json_data[json_id]
		else:
			return None


if __name__ == '__main__':
	oj = OperationJson('login.json')
	# print(oj.get_json()['post'])
	print(oj.get_data('login'))
# json_file = open('../data_config/interface.json')
# json_data = json.load(json_file)
# print(json_data['post'])