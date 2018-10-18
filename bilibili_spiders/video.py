import requests
from base import BaseSpider

class VideoSpider(BaseSpider):
	"""
	"""
	name = "video"
	api_url = "https://api.bilibili.com/x/web-interface/newlist"

	def _crawl_section(self, section_id):
		res = self._make_request(section_id)

	def _make_request(self, section_id, tp=0, pn=1, ps=20):
		payload = {'rid': section_id, 'type': tp, 'pn': pn, 'ps': ps}
		res = requests.get(api_url, payload)
		return res.json()

	def _get_max_page(self, json):
		pass

	def _parse_page(self, json):
		pass

	def crawl_sections(self, section_ids):
		if isinstance(section_ids, list):
			for section_id in section_ids:
				self._records += self._crawl_section(section_id)
		else:
			self._records += self._crawl_section(section_id)
		return self



	
