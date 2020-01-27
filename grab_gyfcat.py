import requests
from bs4 import BeautifulSoup

class gyfcat_reader():

	def __init__(self, file):
		file = _file

	def read_file(self):
		pass

	def parse(self):
		pass


if __name__ == '__main__':

	#inputs = "xxx"
	#gyfcat = gyfcat_reader(inputs)
	#images = gyfcat.parse()

	# text file input here...
	#website = 'https://gfycat.com/impolitegrimyhapuka-animeme'
	website = 'https://gfycat.com/distinctflusteredhind-misunderstood-understand-confused'

	# access the website
	response = requests.get(website)
	#print(response.url)
	#print(type(response))
	#print(response)
	#print(response.text)
	#print(response.content)

	# initialize Beautiful Soup
	soup = BeautifulSoup(response.text, 'html.parser')
	#print(soup.prettify())

	video = soup.find('video', attrs={'class':'video media'})
	print(video)

	links = video.find_all('source')
	print(links)
	for link in links:
		print(link['src'])

	webm_link = video.find('source')
	webm_url = webm_link['src']

	#links = videos.find('source')
	#print(links['src'])

	r = requests.get(webm_url)

	filename = webm_url.split('/')[-1]
	print(filename)

	#with open(filename, 'wb') as f:
	#    f.write(r.content)




