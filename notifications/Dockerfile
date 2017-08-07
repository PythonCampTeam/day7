FROM python:3.5.2
ADD requirements /service/requirements
ENV RABBIT_PASSWORD guest
ENV RABBIT_USER guest
ENV RABBIT_HOST 0.0.0.0
ENV RABBIT_PORT 5672
ENV RABBIT_MANAGEMENT_PORT 15672

WORKDIR /service
COPY config/config.yml /service/config/config.yml
COPY rpc /service/rpc
COPY run.sh /service
WORKDIR /service
RUN chmod +x /service/run.sh
RUN /bin/bash -c "pip3 install -r /service/requirements/base.txt"
#CMD /service/run.sh
#CMD ["nameko","run" "/service/rpc/service_hello"]
