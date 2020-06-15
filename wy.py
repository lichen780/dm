import requests
def start():
	cookies = {
		'MUSIC_U': '158e87e371bc9b8e8bcb2d09543b425c8e786030155986b3048868b55489928833a649814e309366',
		'__csrf': '125dd9726016ed3a44fee21e9f6e44e5',
	}
	res = requests.post('http://yibiwy.fun/api.php?do=sign', cookies=cookies)
	resp = requests.get('http://yibiwy.fun/api.php?do=daka', cookies=cookies)
	print(res.text,resp.text)
def main_handler(event, context):
	return start()
if __name__ == '__main__':
	start()
