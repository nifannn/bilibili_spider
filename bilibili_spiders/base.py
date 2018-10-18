import pandas as pd

class BaseSpider(object):
	"""
	"""
	def __init__(self):
		self._records = []

	@property
	def records(self):
		return self._records

	def to_df(self):
		pass

	def to_csv(self):
		pass

	def to_sql(self):
		pass

	def to_rdb(self):
		pass

	def to_doc_db(self):
		pass

	
