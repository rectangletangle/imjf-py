imjf-py
========

The official Python client for [www.isMyJsFucked.com](http://www.ismyjsfucked.com/). This service is ideal for setting
up quick and dirty smoke tests on your most important URLs.

## Usage
`ismyjsfucked` determines if the JavaScript at a URL is broken. Returning `False` indicates that everything is ok.
`True` indicates that at least one URL is confirmed for being broken. An `IMJFException` is raised when the state of
the JavaScript isn't fully known, or the URL's status code implies failure, i.e., 4XX or 5XX. More information can be
found at [www.isMyJsFucked.com/api/](http://www.ismyjsfucked.com/api/).

```python
>>> from imjf import ismyjsfucked
>>> ismyjsfucked('http://www.ismyjsfucked.com/tests/exception.html')
True
>>> ismyjsfucked('http://www.ismyjsfucked.com/tests/ok.html')
False
>>> urls = ['www.ismyjsfucked.com/tests/ok.html', 'www.ismyjsfucked.com/tests/exception.html']
>>> ismyjsfucked(urls) # returns `True`, because at least one URL is fucked
True
```

## Installation
```sh
$ pip install imjf
```

## Dependencies
* Python 2 or 3
* [requests](http://docs.python-requests.org/)
