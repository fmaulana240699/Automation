FROM	python

RUN	pip3 install PyPI && mkdir app

ADD	https://raw.githubusercontent.com/fmaulana240699/socket-python/master/server.py  app

CMD	python3 /home/server.py

