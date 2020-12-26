FROM python
COPY main.py /main.py
COPY list /list
RUN for i in `cat list`; do curl http://image-net.org/api/text/imagenet.synset.geturls?wnid=$i > $i; done
RUN pip install requests
RUN python /main.py
