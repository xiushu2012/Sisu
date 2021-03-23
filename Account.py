# -*- coding: utf-8 -*-

import akshare as ak
import numpy as np  
import pandas as pd  
import math
import datetime
import os
import matplotlib.pyplot as plt
import openpyxl
from matplotlib.pyplot import MultipleLocator

def get_akshare_account(xlsfile):
	shname='account'
	isExist = os.path.exists(xlsfile)
	if not isExist:
		stock_em_account_df = ak.stock_em_account()
		stock_em_account_df.to_excel(xlsfile,sheet_name=shname)
		
		print("xfsfile:%s create" % (xlsfile))  
	else:
		print("xfsfile:%s exist" % (xlsfile))
	
	return xlsfile,shname



if __name__=='__main__':

		accountpath =  "./%s.xls" % ('account')
		resultpath,insheetname = get_akshare_account(accountpath)
		print("data of path:" + resultpath + ",sheetname:" +insheetname)
		
		
		stock_account_df = pd.read_excel(accountpath, 'account')[['数据日期', '新增投资者-数量','沪深户均市值']]
		stock_account_df = stock_account_df.sort_values('数据日期',ascending=True)

		x_data  =  stock_account_df['数据日期'].values.tolist()
		y_data  =  stock_account_df['新增投资者-数量'].tolist()
		y_data2 =  stock_account_df['沪深户均市值'].tolist()

		#plt.plot(x_data,y_data,color='red',linewidth=2.0,linestyle='--')
		plt.plot(x_data,y_data2,color='blue',linewidth=2.0,linestyle='--')
		plt.xticks(range(len(x_data)),x_data,rotation=270)
		plt.xlabel('time',fontsize=10)
		plt.ylabel('value',fontsize=10)

		x_major_locator=MultipleLocator(1)
		y_major_locator=MultipleLocator(5)
		ax=plt.gca()
		ax.xaxis.set_major_locator(x_major_locator)
		ax.yaxis.set_major_locator(y_major_locator)
		
		#miny = min(min(y_data),min(y_data2)) - 1
		#maxy = max(max(y_data),max(y_data2)) + 1
		
		plt.xlim(min(x_data),max(x_data))
		plt.ylim(min(y_data2),max(y_data2))
		plt.subplots_adjust(bottom=0.3)
		
		imagepath =  r'./account.png'
		plt.savefig(imagepath,dpi=plt.gcf().dpi)
		print("image of path:" + imagepath)
		
		plt.show()






