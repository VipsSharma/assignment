FROM alpine

RUN apk add nginx; 

# CONFIGUTATIONS
# nginx configuration
ADD $PWD/config/nginx.conf /etc/nginx/nginx.conf
ADD $PWD/config/app.conf /etc/nginx/default.d/app.conf

# keys and certs
ADD $PWD/certs/nginx-selfsigned.key   /etc/ssl/private/nginx-selfsigned.key
ADD $PWD/certs/nginx-selfsigned.crt  /etc/ssl/certs/nginx-selfsigned.crt


EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
