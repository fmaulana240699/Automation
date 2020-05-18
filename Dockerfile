FROM	python

RUN	pip3 install PyPI

ADD	https://github.com/fmaulana240699/socket-python/blob/master/server.py  /home/

CMD	python3 /home/server.py

