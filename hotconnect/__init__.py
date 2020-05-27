import requests

class Hotmart:
	def __init__(self, id, secret, key):
		self.id = id
		self.secret = secret
		self.key = key

	def get_token(self):
		method_url = 'https://api-sec-vlc.hotmart.com/security/oauth/token'
		headers = {'Authorization': 'Basic ' + self.key}
		payload = {'grant_type': 'client_credentials', 'client_id' : self.id, 'client_secret': self.secret}

		try:
			r = requests.post(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data['access_token']
		except:
			return None
		
	def get_order(self, product_id=None, start_date=None, end_date=None, status_type=None, 
			email=None, transaction=None, transaction_status=None, buyer_name=None, 
			cpf=None, sales_nature=None, payment_engine=None, show_not_accessed=None,
			payment_type=None, source=None, affiliate_name=None, offer_key=None,
			order_by=None, page=None, rows=None):

		method_url = 'https://api-hot-connect.hotmart.com/reports/rest/v2/history'
		headers = {'Authorization': 'Bearer ' + self.get_token()}
		payload = {}
		
		if product_id:
			payload['productId'] = product_id
		if start_date:
			payload['startDate'] = start_date
		if end_date:
			payload['endDate'] = end_date
		if status_type:
			payload['statusType'] = status_type
		if email:
			payload['email'] = email
		if transaction:
			payload['transaction'] = transaction
		if transaction_status:
			payload['transactionStatus'] = transaction_status
		if buyer_name:
			payload['buyerName'] = buyer_name
		if cpf:
			payload['cpf'] = cpf
		if sales_nature:
			payload['salesNature'] = sales_nature
		if payment_engine:
			payload['paymentEngine'] = payment_engine
		if show_not_accessed:
			payload['showNotAccessed'] = show_not_accessed
		if payment_type:
			payload['paymentType'] = payment_type
		if source:
			payload['source'] = source
		if affiliate_name:
			payload['affiliateName'] = affiliate_name
		if offer_key:
			payload['offerKey'] = offer_key
		if order_by:
			payload['orderBy'] = order_by
		if page:
			payload['page'] = page
		if rows:
			payload['rows'] = rows
		
		try:
			r = requests.get(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data
		except: 
			return None

	def get_purchase_details(self, transaction_status, start_date, end_date, product_id=None, 
			status_type=None, buyer_email=None, transaction=None, page=None, rows=None):

		method_url = 'https://api-hot-connect.hotmart.com/reports/rest/v2/purchaseDetails'
		headers = {'Authorization': 'Bearer ' + self.get_token()}
		payload = {'transactionStatus': transaction_status, 'startDate': start_date, 'endDate': end_date}
		
		if product_id:
			payload['productId'] = product_id
		if buyer_email:
			payload['buyerEmail'] = buyer_email
		if transaction:
			payload['transaction'] = transaction
		if page:
			payload['page'] = page
		if rows:
			payload['rows'] = rows
		
		try:
			r = requests.get(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data
		except: 
			return None