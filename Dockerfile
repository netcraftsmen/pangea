#
#     Copyright (c) 2023 BlueAlly NetCraftsmen, LLC
#     All rights reserved.
#
#     author: @joelwking
#     written:  17 August 2023
#     references:
#       activate virtualenv: https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
#
FROM python:3.10-slim-buster
ENV VIRTUAL_ENV=/opt/pangea
LABEL maintainer="Joel W. King" email="programmable.networks@gmail.com"
RUN apt update && \
    apt -y install git && \
    apt -y install python3-venv && \
    apt -y install python3-dev && \
    apt -y install build-essential && \
    apt -y install curl && \
    pip3 install --upgrade pip 
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#
#
RUN mkdir /src
COPY requirements.txt /src
WORKDIR /src
RUN pip install -r requirements.txt
#
