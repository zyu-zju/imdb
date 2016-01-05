"""Script to gather IMDB keywords from 2015's top grossing movies"""

import sys

URL = 'http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us,desc&start=1&year=2015,2015'

def main():
	"""Main entry point for the script"""
	pass

def get_top_grossing_movie_links(url):
	"""Return a list of tuples containing the top grossing movies of 2015 and link to their IMDB
	page."""
	pass

def get_keywords_for_move(url):
	"""Return a list of keywords associated with *movie*"""
	pass

if __name__ == '__main__':
	sys.exit(main())