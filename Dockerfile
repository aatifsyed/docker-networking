FROM python

RUN python -m pip install pandas
RUN python -m pip install ipython

WORKDIR "/dataserver"

COPY server.py .

CMD ["python", "server.py"]