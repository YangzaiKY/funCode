import urllib.request as urlrequest

def getRemoteFileSize(url, proxy=None):
	opener = urlrequest.build_opener()
	if proxy:
		if url.lower().startswith('https://'):
			opener.add_handler(urlrequest.ProxyHandler({'https': proxy}))
		else:
			opener.add_handler(urlrequest.ProxyHandler({'http': proxy}))
	try:
		request = urlrequest.Request(url)
		request.get_method = lambda: 'HEAD'
		response = opener.open(request)
		response.read()
	except Exception:
		return 0
	else:
		# print(response.headers)
		file_size = dict(response.headers).get('Content-Length', 0)
		return int(file_size)


if __name__ == '__main__':
	url = {'model': [# ResNets (with imprv)
					 'FCOS_imprv_R_50_FPN_1x',
					 'FCOS_imprv_dcnv2_R_50_FPN_1x',
					 'FCOS_imprv_R_101_FPN_2x',
					 'FCOS_imprv_dcnv2_R_101_FPN_2x',
					 'FCOS_imprv_X_101_32x8d_FPN_2x',
					 'FCOS_imprv_dcnv2_X_101_32x8d_FPN_2x',
					 'FCOS_imprv_X_101_64x4d_FPN_2x',
					 'FCOS_imprv_dcnv2_X_101_64x4d_FPN_2x',
					 # ResNets (without imprv)
					 'FCOS_R_50_FPN_1x',
					 'FCOS_R_101_FPN_2x',
					 'FCOS_X_101_32x8d_FPN_2x',
					 'FCOS_X_101_64x4d_FPN_2x',
					 # MobileNets
					 'FCOS_syncbn_bs32_c128_MNV2_FPN_1x',
					 'FCOS_syncbn_bs32_MNV2_FPN_1x',
					 'FCOS_bn_bs16_MNV2_FPN_1x'],
		   'url': ['https://cloudstor.aarnet.edu.au/plus/s/ZSAqNJB96hA71Yf/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/plKgHuykjiilzWr/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/hTeMuRa4pwtCemq/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/xq2Ll7s0hpaQycO/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/WZ0i7RZW5BRpJu6/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/08UK0OP67TogLCU/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/rKOJtwvJwcKVOz8/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/jdtVmG7MlugEXB7/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/dDeDPBLEAt19Xrl/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/vjL3L0AW7vnhRTo/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/U5myBfGF7MviZ97/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/wpwoCi4S8iajFi9/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/3GKwaxZhDSOlCZ0/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/OpJtCJLj104i2Yc/download',
		   		   'https://cloudstor.aarnet.edu.au/plus/s/B6BrLAiAEAYQkcy/download']}

	max_model_name_length = max([len(m) for m in url['model']])
	files_size = []
	for model, url in zip(url['model'], url['url']):
		file_size = getRemoteFileSize(url)
		print('model: {0:{1}}  size: {2:8.2f}MB'.format(model, max_model_name_length, file_size/1024/1024))
