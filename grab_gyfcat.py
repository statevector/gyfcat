import requests
from bs4 import BeautifulSoup

def import_text(file, verbose=False):
	text = open(file, 'r')
	urls = text.readlines()
	text.close()
	urls = [url.rstrip('\n') for url in urls]
	if len(urls) == 0:
		quit('Error: Input text file empty')
	if verbose:
		print('Loaded the following URLs:')
		print('\n'.join('{}: {}'.format(*url) for url in enumerate(urls)))
	return urls

def make_soup(url):
	page = requests.get(url)
	return BeautifulSoup(page.text, 'html.parser')

def get_image(url, verbose=False):
	bs = make_soup(url)
	# find page's <video> tag
	video = bs.find('video', attrs={'class':'video media'})
	if verbose: 
		print('<video> tag: {}'.format(video))
	# isolate webm link associated with <source> tag under <video>
	link = video.find('source', attrs={'type':'video/webm'})['src']
	if verbose: 
		print('<source> tag: {}'.format(links))
	if link is "":
		quit('Error: BS <source> tag not found')
	return link

def write_image(url):
	filename = url.split('/')[-1]
	r = requests.get(url)
	if r.status_code == 200:
		try:
			with open(filename, 'wb') as f:
				f.write(r.content)
			return 'File '+filename+' written successfully'
		except:
			return 'Error: unable to write '+filename+'.'
	else:
		return 'Error: HTTP Status Code is not 200'

if __name__ == '__main__':

	# read in list of gyfcat webpage URLs
	page_urls = import_text('gyfcat.txt', verbose=True)

	# iterate over the list
	for page_url in page_urls:
		# extract the url pointing to the image on the gyfcat page
		image_url = get_image(page_url)
		# save the image locally
		result = write_image(image_url)
		print(result)



