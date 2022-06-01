FROM debian:bullseye

RUN apt update
RUN apt install -y make gcc

WORKDIR /root
ADD openssl  /root/openssl

WORKDIR /root/openssl
RUN ./config && make && make install

WORKDIR /root
ENV PATH="/usr/local/ssl/bin/:${PATH}"

# https://superhero.ninja/2015/07/22/create-a-simple-https-server-with-openssl-s_server/
RUN printf "\n\n\n\n\n\n\n\n\n\n" | openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

EXPOSE 443/tcp

# https://superhero.ninja/2015/07/22/create-a-simple-https-server-with-openssl-s_server/
ENTRYPOINT openssl s_server -key key.pem -cert cert.pem -accept 443 -www
