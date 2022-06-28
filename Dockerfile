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

ADD nginx-1.23.0  /root/nginx-1.23.0

WORKDIR /root/nginx-1.23.0
RUN ./configure --with-openssl=../openssl --with-http_ssl_module --without-http_rewrite_module --without-http_gzip_module
RUN make && make install
ADD nginx.conf /usr/local/nginx/conf/nginx.conf
WORKDIR /root

ADD entrypoint.sh /root/entrypoint.sh
ADD tail_error.sh /root/tail_error.sh
ADD tail_access.sh /root/tail_access.sh

# now php ...
RUN apt install -y php-fpm

EXPOSE 80/tcp
EXPOSE 443/tcp

# https://superhero.ninja/2015/07/22/create-a-simple-https-server-with-openssl-s_server/
#ENTRYPOINT openssl s_server -key key.pem -cert cert.pem -accept 443 -www
ENTRYPOINT /root/entrypoint.sh
