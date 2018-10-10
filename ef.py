import xlrd,xlwt
import re

class ExcelFile():
	#初始化excel文件
	def __init__(self,filename):
		workbook = xlrd.open_workbook(filename)
		sheetR = workbook.sheet_by_index(0)
		sheetName = sheetR.name

		f = xlwt.Workbook()#创建工作簿
		sheet = f.add_sheet(filename,cell_overwrite_ok=True)#创建工作表
		


		self.workbook = workbook
		self.sheetName = sheetName

	def Read(self):
		#读取客户定单 
		if self.sheetName == 'Order' :
			pass
		#读取盘点库存
		if self.sheetName == 'Stock' :
			pass
		#读取生产实绩
		if self.sheetName == 'production' :
			pass
		#读取采购实绩
		if self.sheetName == 'Purchase' :
			pass

	def WriteOrder(self):
		#生成客户定单模板
		pass
		#定单数据


	def WriteStock(self):
		#生成库存盘点模板
		pass

	def WriteProduction(self):
		#生成生产计划表（自动货）
		pass

	def WritePurchase(self):
		#生成采购模板（自动化）
		pass
