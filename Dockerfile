FROM	python

RUN	pip3 install PyPI

COPY	server.py /home/.

CMD	python3 /home/server.py

