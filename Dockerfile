FROM python

RUN python -m pip install pandas
RUN python -m pip install ipython
RUN python -m pip install requests

WORKDIR "/dataserver"

COPY server.py .
COPY client.py .

CMD ["python", "server.py"]